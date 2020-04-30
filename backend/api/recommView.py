from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Store, BHour, Menu, Review

from .serializers import StoreSerializer
import math
import pandas as pd
import numpy as np
from django.db.models import Count, Avg
from scipy.sparse.linalg import svds

from .models import Review

reviews = Review.objects.all()
stores = Store.objects.all()


def getStoresAround(lat, lng, area):
    R = 6378.137
    filter_data = []

    tmp = stores.filter(address__contains=area)

    for data in tmp.values():
        if data.get('latitude') is None:
            continue

        store_lat = float(data.get('latitude'))
        store_lng = float(data.get('longitude'))

        # print(store_lat, store_lng)
        dLat = abs(store_lat * math.pi / 180.0 - lat * math.pi / 180.0)
        dLng = abs(store_lng * math.pi / 180.0 - lng * math.pi / 180.0)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat * math.pi / 180) * \
            math.cos(store_lat * math.pi / 180) * \
            math.sin(dLng / 2) * math.sin(dLng / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        if d * 1000 <= 3000:  # 3km 이내
            filter_data.append(data)

    # 스토어 dataframe 만들기
    store_df = pd.DataFrame(filter_data)

    # 리뷰
    queryset = reviews.filter(store_id__in=list(store_df['id']))

    return queryset


def cal_rmse(user_rating, predicted_user_rating):
    rmse = 0.0
    cnt = 0
    for i in range(len(user_rating)):
        for j in range(len(user_rating[0])):
            if user_rating[i, j] != 0:
                # print(user_rating[i, j], predicted_user_rating[i, j])
                rmse += (user_rating[i, j] -
                         predicted_user_rating[i, j])**2
                cnt += 1

    return (rmse/cnt)**0.5


@api_view(['GET'])
def recommand_based_user(request, id=None):
    # params
    params = request.GET
    print(params.dict())
    lat = float(params.get('latitude'))
    lng = float(params.get('longitude'))
    area = params.get('area')
    users = params.getlist('users')
    # users = params.getlist('users[]')
    users.append(id)

    print(users)  # (68632, 539244, 21180, 209301)

    queryset = getStoresAround(lat, lng, area)  # 주변 음식점들의 리뷰들

    user_review = queryset.filter(
        user_id__in=users)  # 유저가 리뷰한 것 전국 : 191개 마포구: 10개 ㅎ

    print("유저(들)의 해당지역 리뷰 개수 : {}".format(len(user_review)))

    # 유저의 리뷰수가 0개 : popular 순으로
    # 유저의 리뷰수가 1~4개 : contents 기반 추천
    # 유저의 리뷰가 5개 이상 : MF

    if len(user_review) == 0:
        print('popularity based recommand..')

        semires = queryset.values('store_id').annotate(
            count=Count('store_id')).order_by('-count').values('store_id', 'count')[:20]  # 리뷰가 많은 순 상위 20개

        result = stores.filter(id__in=[item.get('store_id')
                                       for item in semires.values('store_id')])  # 추출된 리뷰들의 음식점정보

        return Response({"result": result.values()}, status.HTTP_200_OK)

    elif len(user_review) > 0 and len(user_review) < 5:

        print('contents based recommand..')
        # print(len(user_review))
        other_user = []
        for item in list(user_review):  # 현재 유저가 리뷰한 것들
            # print(item)
            item_review = queryset.filter(store_id=item.store)
            for user in list(item_review):
                other_user.append(user.user_id)  # 같은 음식점을 리뷰한 유저들

        other_user = list(set(other_user))  # 중복제거
        # print(other_user)

        semires = queryset.filter(user_id__in=other_user, score_gte=3).values(
            'store_id').annotate(count=Count('store_id')).order_by('-count').values('store_id', 'count')[:20]  # 중복, 상위 20개

        result = stores.filter(id__in=[item.get('store_id')
                                       for item in semires.values('store_id')])  # 추출된 리뷰들의 음식점정보

        return Response({"result": result.values()}, status.HTTP_200_OK)

    else:
        print('matrix factorization based recommand..')

        # testsurprise(queryset)
        # return Response({"result": None}, status.HTTP_200_OK)

        dataframe = pd.DataFrame(list(queryset.values()))

        if len(users) > 1:

            # 새로만든 동행자포함 합체인물
            result = queryset.filter(user_id__in=users).values('store_id').annotate(
                score=Avg('score')).values('store_id', 'score')
            df = pd.DataFrame(result)
            df['user_id'] = id

            dataframe = dataframe[~dataframe.user_id.isin(users)]
            dataframe = dataframe.append(df)

        user_rating = pd.pivot_table(
            dataframe, index='user_id', columns='store_id', values='score').fillna(0)
        R = user_rating.as_matrix()
        print(f'매트릭스 R의 d {R.shape}dfd')

        # SVD
        # R = (Nxk)(kxM) MF R.shape-1  SVD = U(sigma)Vt
        k = int(min(R.shape) / 25)
        U, sigma, Vt = svds(R, k=k)
        sigma = np.diag(sigma)  # 대각행렬로 바꿈

        # 다시 matrix 만들기
        svd_user_predicted_ratings = np.dot(
            np.dot(U, sigma), Vt)

        # rmse 측정
        # rmse = cal_rmse(R, svd_user_predicted_ratings)
        # print("k={} 일때 MF rmse : {}".format(k, rmse))

        svd_df = pd.DataFrame(svd_user_predicted_ratings, columns=list(
            user_rating.columns.values), index=list(user_rating.index.values))

        # 평점이 높은 상위 15개
        svd_user = svd_df.ix[id].sort_values(ascending=False).head(15)

        result = stores.filter(id__in=list(svd_user.index.values))
        # print(type(svd_user))

        # k=15 일때 MF rmse : 3.488315409672258
        # k=30 일때 MF rmse : 3.2105433783469404
        # k=100 일때 MF rmse : 2.4704298644120493

        return Response(result.values(), status.HTTP_200_OK)
