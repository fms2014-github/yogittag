from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Store, BHour, Menu, Review, User

from .serializers import BhourSerializer, UserSerializer, StoreSerializer, ReviewSerializer, MenuSerializer, FollowSerializer, FavoriteListSerializer, FavoriteStoreSerializer
import math

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
queryset = Store.objects.all()


@api_view(['GET'])
def detail(requset, id=None):
    # id = requset.GET.get('id')
    print(id)
    result = queryset.filter(id__exact=id)
    return Response({'result': result.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def store_find_by_name(request):
    # 검색 요청 정보 가져오기
    params = request.GET
    print(params.dict())
    if params.dict() != {}:
        print('params Check')
        keyword = params.get('keyword')
        lat = float(params.get('latitude'))
        lng = float(params.get('longitude'))
        category = params.getlist('category')  # dict에 key값이 이렇게 들어가서 수정
        distance = params.get('distance')
        if keyword is not None:
            keyword_result = queryset.filter(Q(store_name__contains=keyword) | Q(category__contains=keyword))
        else:
            area = params.get('area')
            keyword_result = queryset.filter(address__contains=area)
        filter_data1 = []
        filter_data2 = []
        print(lat, lng, category, distance)
        R = 6378.137
        if distance is not None:
            for data in keyword_result.values():
                store_lat = float(data.get('latitude'))
                store_lng = float(data.get('longitude'))
                dLat = abs(store_lat * math.pi / 180.0 - lat * math.pi / 180.0)
                dLng = abs(store_lng * math.pi / 180.0 - lng * math.pi / 180.0)
                a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat * math.pi / 180) * \
                    math.cos(store_lat * math.pi / 180) * \
                    math.sin(dLng / 2) * math.sin(dLng / 2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                d = R * c
                # print(d*1000)
                if d * 1000 < int(distance):
                    filter_data1.append(data)
        else:
            print('????')
            for data in keyword_result.values():
                store_lat = float(data.get('latitude'))
                store_lng = float(data.get('longitude'))
                dLat = abs(store_lat * math.pi / 180.0 - lat * math.pi / 180.0)
                dLng = abs(store_lng * math.pi / 180.0 - lng * math.pi / 180.0)
                a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat * math.pi / 180) * \
                    math.cos(store_lat * math.pi / 180) * \
                    math.sin(dLng / 2) * math.sin(dLng / 2)
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                d = R * c
                # print(d*1000)
                if d * 1000 < 500:
                    filter_data1.append(data)
        result = filter_data1
        print(len(result))
        if len(category) > 0:   # is not None 에 아무것도 없어도 들어가서 바꿨습니다
            for data in result:
                for cat in category:
                    print(cat)
                    print(data.get('category'))
                    print(data.get('category').find(cat))
                    if data.get('category').find(cat) > -1:
                        filter_data2.append(data)
                        break
            result = filter_data2   # 요게 for문 바깥에 있어서 tap

        return Response({'result': result}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bhour_find_by_store(request, id=None):
    result = BHour.objects.filter(store_id__exact=id)
    return Response({"result": result.values()}, status.HTTP_200_OK)


@api_view(['GET'])
def menu_find_by_store(request, id=None):
    result = Menu.objects.filter(store_id__exact=id)
    return Response({"result": result.values()}, status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def review_find_by_store(request, id=None):
    if request.method == 'GET':
        riviews = Review.objects.filter(
            store=id).select_related('user').order_by('-id')
        return Response({"result": riviews.values()}, status.HTTP_200_OK)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
            # return JsonResponse({serializer.data}, status=200)
        return JsonResponse(serializer.errors, status=400)
