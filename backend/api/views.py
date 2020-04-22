# HTTP 상태 코드 객체
from rest_framework import status
# REST Method 설정 데코레이션
from rest_framework.decorators import api_view
from backend.settings import SECRET_KEY
from rest_framework.response import Response

import requests

from .models import bhour, menu, review, Store as store, user

from .serializers import BhourSerializer, UserSerializer, StoreSerializer, ReviewSerializer, MenuSerializer

import time
import json
import hashlib
import base64

import math


# user start
@api_view(['POST'])
def user_login(request):
    input_email = request.data.get('email')
    input_password = request.data.get('password')
    try:
        # 계정 확인
        email = user.objects.all().get(email__exact=input_email,
                                       password__exact=input_password)

        # JWT 객체
        header = {"typ": "jwt", "alg": "HS256"}
        payload = {"aud": email.email, "sub": "login", "iat": time.time().__int__(),
                   "exp": (time.time().__int__() + 50)}
        signature = hashlib.sha256(base64.b64encode(repr(header).encode()) +
                                   base64.b64encode(repr(payload).encode()) +
                                   SECRET_KEY.encode())

        # jwt 토큰 생성
        jwt = base64.b64encode(repr(header).encode()).decode("UTF-8") + '.' + \
            base64.b64encode(repr(payload).encode()).decode("UTF-8") + '.' + \
            base64.b64encode(signature.hexdigest().encode()).decode()

    except:
        return Response('Not Found Account', status=status.HTTP_400_BAD_REQUEST)

    return Response({"jwt": jwt}, status=status.HTTP_200_OK)


@api_view(['POST'])
def session_refresh(request):
    # JWT 토큰 획득
    get_jwt = request.data.get("jwt").split('.')
    print(get_jwt[0])
    print(get_jwt[1])
    # JWT 토큰 검증
    if hashlib.sha256(get_jwt[0].encode() +
                      get_jwt[1].encode() +
                      SECRET_KEY.encode()).hexdigest() == base64.b64decode(get_jwt[2]).decode():
        # 토큰이 정상이면 payload 해석
        payload = json.loads(base64.b64decode(
            get_jwt[1]).decode().replace("'", "\""))
        print(payload['exp'], int(time.time().__int__()))
        # 토큰 유효기간 검증
        if int(payload['exp']) >= int(time.time().__int__()):
            # 토큰 유효기간이 지나지 않았을 경우 유효기간 갱신
            payload['iat'] = time.time().__int__()
            payload['exp'] = time.time().__int__() + 50
            get_jwt[1] = base64.b64encode(
                repr(payload).encode()).decode("UTF-8")
            get_jwt[2] = base64.b64encode(hashlib.sha256(
                get_jwt[0].encode() + get_jwt[1].encode() + SECRET_KEY.encode()).hexdigest().encode()).decode("UTF-8")

            return Response({"jwt": '.'.join(get_jwt)}, status=status.HTTP_200_OK)
        else:
            # 유효기간이 지났을 경우 로그아웃
            return Response({"error": "logout"}, status=status.HTTP_400_BAD_REQUEST)
    # 토큰 정보가 없거나 검증에 실패했을 경우 세션 삭제
    return Response({"jwt": ''}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = UserSerializer(data=data)

    # 데이터 유효성 검사
    if serializer.is_valid():
        user = user(**data)
        user.save()
        return Response({"success": "sign up"}, status=status.HTTP_200_OK)
    return Response({"error": "Bad_Request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def user_delete(request):
    # JWT 토큰 획득
    get_jwt = request.data.get("jwt").split('.')

    # JWT 토큰 검증
    if hashlib.sha256(get_jwt[0].encode() +
                      get_jwt[1].encode() +
                      SECRET_KEY.encode()).hexdigest() == base64.b64decode(get_jwt[2]).decode():
        # 토큰이 정상이면 payload 해석
        payload = json.loads(base64.b64decode(
            get_jwt[1]).decode().replace("'", "\""))
        print(payload['exp'], int(time.time().__int__()))
        # 토큰 유효기간 검증
        if int(payload['exp']) >= int(time.time().__int__()):
            # 토큰 유효기간이 지나지 않았을 경우 회원 이메일 추출
            get_email = payload['aud']
            user = user.objects.get(email__exact=get_email)
            user.delete()
            return Response({"jwt": '.'.join(get_jwt)}, status=status.HTTP_200_OK)
        else:
            # 유효기간이 지났을 경우 로그아웃
            return Response({"success": "delete user"}, status=status.HTTP_400_BAD_REQUEST)
    # 토큰 정보가 없거나 검증에 실패했을 경우 세션 삭제
    return Response({"jwt": ''}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_list(request):
    raise None


@api_view(['POST'])
def oauth_code_google(request):
    oauthResult = request.data.get("oauthCode")
    tokenRequestURL = 'https://oauth2.googleapis.com/token'
    data = {
        'code': oauthResult["code"],
        'client_id': '25608544222-lfe7jdkikoef92jgt45mvhe83ts98n80.apps.googleusercontent.com',
        'client_secret': 'MjwjwsVlExjXdivmhrIq-CiU',
        'redirect_uri': 'http://localhost:8080/google-auth',
        'grant_type': 'authorization_code',
    }
    res = requests.post(tokenRequestURL, data=data)
    print(res.json())
    print(res.json()['access_token'])
    access_token = res.json()['access_token']
    print(res.json()['token_type'])
    Authorization = res.json()['token_type']
    headers = {'Authorization': Authorization + ' ' + access_token}
    userInfoRequsetURL = 'https://people.googleapis.com/v1/people/me?personFields=birthdays&personFields=names&personFields=nicknames&personFields=genders'

    res = requests.get(userInfoRequsetURL, headers=headers)
    print(res.json())
    refresh_token_URL = 'https://oauth2.googleapis.com/token'
    data = {
        'client_id': '25608544222-lfe7jdkikoef92jgt45mvhe83ts98n80.apps.googleusercontent.com',
        'client_secret': 'MjwjwsVlExjXdivmhrIq-CiU',
        'refresh_token': access_token,
        'grant_type': 'refresh_token',
    }
    res = requests.post(refresh_token_URL, data=data)
    print(res.json())
    return Response('', status=status.HTTP_200_OK)


@api_view(['POST'])
def oauth_code_naver(request):
    oauthResult = request.data.get("oauthCode")
    tokenRequestURL = 'https://nid.naver.com/oauth2.0/token'
    data = {
        'code': oauthResult["code"],
        'client_id': 'ISrEReGthtZMH67maTLZ',
        'client_secret': 'kCOv4mVaGK',
        'redirect_uri': 'http://localhost:8080/naver-auth',
        'grant_type': 'authorization_code',
    }
    res = requests.post(tokenRequestURL, data=data)
    print(res.json()['access_token'])
    access_token = res.json()['access_token']
    print(res.json()['token_type'])
    Authorization = res.json()['token_type']
    headers = {'Authorization': Authorization + ' ' + access_token}
    userInfoRequsetURL = 'https://openapi.naver.com/v1/nid/me'
    res = requests.get(userInfoRequsetURL, headers=headers)
    print(res.json())
    return Response('', status=status.HTTP_200_OK)


# user end

# bhour start
@api_view(['POST'])
def bhour_find_by_store(request):
    get_store = request.data.get('store')

    result_menu = bhour.objects.filter(store__exact=get_store)
    return Response({"result": result_menu}, status.HTTP_200_OK)


# bhour end

# menu start
@api_view(['POST'])
def menu_find_by_store(request):
    get_store = request.data.get('store')

    result_menu = menu.objects.filter(store__exact=get_store)
    return Response({"result": result_menu}, status=status.HTTP_200_OK)


# menu end

# review start
@api_view(["POST"])
def review_find_by_store(request):
    get_store = request.data.get('store')

    find_review = review.objects.filter(store__exact=get_store)
    return Response({"result": find_review}, status=status.HTTP_200_OK)


def review_find_by_user(request):
    get_user = request.data.get('user')

    find_review = review.objects.filter(user__exact=get_user)
    return Response({"result": find_review}, status=status.HTTP_200_OK)


# review end

# store start
@api_view(['POST'])
def store_find_by_name(request):
    print('dd')
    # 검색 요청 정보 가져오기
    get_name = request.data.get('name')
    get_latitude = request.data.get('latitude')
    get_longitude = request.data.get('longitude')
    # get_name = request.data
    # print(get_name)
    result_search = store.objects.filter(store_name__contains=get_name)

    print(result_search[0].longitude)

    for res in result_search:
        # distance = math.acos(math.sin(dLat1)*math.sin(dLat2) + math.cos(dLat1)
        distance = Distance(get_latitude, get_longitude,
                            res.latitude, res.longitude)
        #                       * math.cos(dLat2)*math.cos(dLon1 - dLon2))

        print(distance)

    return Response({"result": result_search.values()}, status=status.HTTP_200_OK)


def Distance(lat1, lon1, lat2, lon2):
    theta = lon1 - lon2
    dist = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2))
    + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.cos(deg2rad(theta))

    dist = math.acos(dist)
    dist = rad2deg(dist)
    dist = dist * 60 * 1.1515
    # dist = dist * 1.609344

    return dist


def deg2rad(deg):

    return (deg * math.pi / 180.0)


def rad2deg(rad):

    return (rad * 180.0 / math.pi)

# store end
