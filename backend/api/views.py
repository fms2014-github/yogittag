from django.core.exceptions import ObjectDoesNotExist
import json

from datetime import datetime

# HTTP 상태 코드 객체
from rest_framework import status
# REST Method 설정 데코레이션
from rest_framework.decorators import api_view
from backend.settings import SECRET_KEY
from rest_framework.response import Response

import requests

from .models import BHour, Menu, Review, Store, User, FavoriteList, FavoriteStore

from .serializers import BhourSerializer, UserSerializer, StoreSerializer, ReviewSerializer, MenuSerializer, FollowSerializer, FavoriteListSerializer, FavoriteStoreSerializer, GoogleAuthSerializer

import time
import json
import hashlib
import base64

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
''' 
# user models
@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print('put')
        print(user.email, user.id, user.name)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data)
        else:
            print('not valid')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def followers_list(request, fId):
    """
    Retrieve, update or delete a code user.followers.
    """
    try:
        user = User.objects.get(pk=fId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FollowSerializer(user)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def followers_detail(request, fId, tId):
    """
    Retrieve, update or delete a code user.followers.
    """
    try:
        user = User.objects.get(pk=fId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        # print(request.data)
        user.followers.add(tId)
        serializer = FollowSerializer(fId, data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 '''
# user models
@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# followers
@api_view(['GET'])
def followers_list(request, fId):
    """
    Retrieve, update or delete a code user.followers.
    """
    try:
        user = User.objects.get(pk=fId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FollowSerializer(user)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def followers_detail(request, fId, tId):
    """
    Retrieve, update or delete a code user.followers.
    """
    try:
        user = User.objects.get(pk=fId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        # 언팔로우 -> 팔로우
        if not user.followers.filter(id=tId).count():
            user.followers.add(tId)
            return Response(tId, status=status.HTTP_200_OK)
        return Response("Already follow", status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # 팔로우 -> 언팔로우
        if user.followers.filter(id=tId).count():
            user.followers.remove(tId)
            return Response(tId, status=status.HTTP_200_OK)
        return Response("Do not follow", status=status.HTTP_400_BAD_REQUEST)

# favorite
@api_view(['GET'])
def favorite_list_all(request):
    """
    List all code favorite_all_list
    """
    if request.method == 'GET':
        favorite_list = FavoriteList.objects.all()
        serializer = FavoriteListSerializer(favorite_list, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def favorite_list_list(request, pk):
    """
    Retrieve, create a new favorite.
    """

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        favorite_list = FavoriteList.objects.filter(user=pk)
        serializer = FavoriteListSerializer(favorite_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["user"] = pk
        serializer = FavoriteListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def favorite_store_list_all(request, pk):
    if request.method == 'GET':
        favorite_store = FavoriteStore.objects.filter(user=pk)
        serializer = FavoriteStoreSerializer(favorite_store, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def favorite_list_detail(request, pk, pk2):
    if request.method == 'GET':
        favorite_store = FavoriteStore.objects.filter(
            user=pk, favorite_list_id=pk2)
        serializer = FavoriteStoreSerializer(favorite_store, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data["user"] = pk
        data["favorite_list_id"] = pk2
        serializer = FavoriteStoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def favorite_store_detail(request, pk, pk2, pk3):
    try:
        favorite_store = FavoriteStore.objects.get(
            user=pk, favorite_list_id=pk2, store=pk3)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        favorite_store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# user start
@api_view(['POST'])
def user_login(request):
    input_email = request.data.get('email')
    input_password = request.data.get('password')
    try:
        # 계정 확인
        email = User.objects.all().get(email__exact=input_email,
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
    get_jwt = request.data.get('jwt').split('.')
    dt = datetime.now().microsecond
    jwt_iss = json.loads(base64.b64decode(
        get_jwt[1] + ("=" * ((4 - len(get_jwt[1]) % 4) % 4))).decode("UTF-8").replace('\'', '\"')).get('iss')
    jwt_exp = json.loads(base64.b64decode(
        get_jwt[1] + ("=" * ((4 - len(get_jwt[1]) % 4) % 4))).decode("UTF-8").replace('\'', '\"')).get('exp')
    if jwt_iss == 'https://accounts.google.com':
        if dt < jwt_exp:
            email = request.data.get('email')
            refresh_token = User.objects.get(
                email__exact=email).google_refresh_token
            refresh_token_url = 'https://oauth2.googleapis.com/token'
            data = {
                'client_id': '25608544222-lfe7jdkikoef92jgt45mvhe83ts98n80.apps.googleusercontent.com',
                'client_secret': 'MjwjwsVlExjXdivmhrIq-CiU',
                'refresh_token': refresh_token,
                'grant_type': 'refresh_token',
            }
            refresh_token = requests.post(refresh_token_url, data=data)
            # 토큰 정보가 없거나 검증에 실패했을 경우 세션 삭제
            return Response({'session': {"email": email, "jwt": refresh_token.json()['id_token']}}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif jwt_iss == 'https://nid.naver.com':
        if dt < jwt_exp:
            email = request.data.get('email')
            refresh_token = User.objects.get(
                email__exact=email).naver_refresh_token
            refresh_token_url = 'https://nid.naver.com/oauth2.0/token?grant_type=refresh_token&client_id=ISrEReGthtZMH67maTLZ&client_secret=kCOv4mVaGK&refresh_token=' + refresh_token
            refresh_token = requests.get(refresh_token_url)

            headers = {'Authorization': refresh_token.json(
            )['token_type'] + ' ' + refresh_token.json()['access_token']}
            userInfoRequsetURL = 'https://openapi.naver.com/v1/nid/me'
            userinfo = requests.get(userInfoRequsetURL, headers=headers)
            jwt_sub = json.loads(
                base64.b64decode(get_jwt[1] + ("=" * ((4 - len(get_jwt[1]) % 4) % 4))).decode("UTF-8").replace('\'', '\"')).get('sub')
            if jwt_sub != userinfo.json()['response']['id']:
                print("???")
                return Response(status=status.HTTP_400_BAD_REQUEST)
            header = {"typ": "jwt", "alg": "HS256"}
            payload = {"iss": 'https://nid.naver.com',
                       "email": userinfo.json()['response']['email'],
                       "sub": userinfo.json()['response']['id'],
                       "profile_image": userinfo.json()['response']['profile_image'],
                       "name": userinfo.json()['response']["name"],
                       "iat": time.time().__int__(),
                       "exp": (time.time().__int__() + 3600)}
            signature = hashlib.sha256(base64.b64encode(repr(header).encode()) +
                                       base64.b64encode(repr(payload).encode()) +
                                       SECRET_KEY.encode())

            # jwt 토큰 생성
            jwt = base64.b64encode(repr(header).encode()).decode("UTF-8") + '.' + \
                base64.b64encode(repr(payload).encode()).decode("UTF-8") + '.' + \
                base64.b64encode(signature.hexdigest().encode()).decode()

            return Response({'session': {
                'email': userinfo.json()['response']['email'],
                'jwt': jwt,
            }}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


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
            user = User.objects.get(email__exact=get_email)
            user.delete()
            return Response({"jwt": '.'.join(get_jwt)}, status=status.HTTP_200_OK)
        else:
            # 유효기간이 지났을 경우 로그아웃
            return Response({"success": "delete user"}, status=status.HTTP_400_BAD_REQUEST)
    # 토큰 정보가 없거나 검증에 실패했을 경우 세션 삭제
    return Response({"jwt": ''}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def oauth_code_google(request):
    oauthResult = request.data.get("oauthCode")
    tokenRequestURL = 'https://oauth2.googleapis.com/token'
    print(oauthResult["code"])
    data = {
        'code': oauthResult["code"],
        'client_id': '25608544222-lfe7jdkikoef92jgt45mvhe83ts98n80.apps.googleusercontent.com',
        'client_secret': 'MjwjwsVlExjXdivmhrIq-CiU',
        'redirect_uri': 'http://localhost:8080/google-auth',
        'grant_type': 'authorization_code',
    }
    auth_data = requests.post(tokenRequestURL, data=data)

    print('auth_data-----------------')
    print(auth_data.json())

    headers = {'Authorization': auth_data.json(
    )['token_type'] + ' ' + auth_data.json()['access_token']}
    userInfoRequsetURL = 'https://www.googleapis.com/oauth2/v2/userinfo'
    userinfo = requests.get(userInfoRequsetURL, headers=headers)

    print('user_info------------------------')
    print(userinfo.json())
    try:

        find_user = User.objects.get(email__exact=userinfo.json()['email'])
        print(find_user)
        serializer = GoogleAuthSerializer(find_user, data={
            'google_refresh_token': auth_data.json()['refresh_token']}, partial=True)
        if serializer.is_valid():
            serializer.save()
    except User.DoesNotExist:
        serializer = GoogleAuthSerializer(data={
            'name': userinfo.json()['name'],
            'email': userinfo.json()['email'],
            'google_refresh_token': auth_data.json()['refresh_token'],
            'profile_picture': userinfo.json()['picture']
        })

        if serializer.is_valid():
            serializer.save()

    user_id = User.objects.get(email__exact=userinfo.json()[
                               'email']).id
    print(user_id)
    return Response({'session': {'email': userinfo.json()['email'],
                                 'jwt': auth_data.json()['id_token'],
                                 'userid': user_id}}, status=status.HTTP_200_OK)


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
    auth_data = requests.post(tokenRequestURL, data=data)
    print(auth_data.json())
    print(auth_data.json()['access_token'])
    print(auth_data.json()['refresh_token'])
    headers = {'Authorization': auth_data.json(
    )['token_type'] + ' ' + auth_data.json()['access_token']}
    userInfoRequsetURL = 'https://openapi.naver.com/v1/nid/me'
    userinfo = requests.get(userInfoRequsetURL, headers=headers)
    print(userinfo.json()['response'])
    try:
        find_user = User.objects.get(
            email__exact=userinfo.json()['response']['email'])
        serializer = UserSerializer(find_user, data={
                                    'naver_refresh_token': auth_data.json()['refresh_token']}, partial=True)
        if serializer.is_valid():
            serializer.save()
    except ObjectDoesNotExist:
        serializer = UserSerializer(data={
            'email': userinfo.json()['response']['email'],
            'naver_refresh_token': auth_data.json()['refresh_token'],
            'profile_picture': userinfo.json()['response']['profile_image']
        })
        if serializer.is_valid():
            serializer.save()
    # JWT 객체
    header = {"typ": "jwt", "alg": "HS256"}
    payload = {"iss": 'https://nid.naver.com',
               "email": userinfo.json()['response']['email'],
               "sub": userinfo.json()['response']['id'],
               "profile_image": userinfo.json()['response']['profile_image'],
               "name": userinfo.json()['response']["name"],
               "iat": time.time().__int__(),
               "exp": (time.time().__int__() + 3600)}
    signature = hashlib.sha256(base64.b64encode(repr(header).encode()) +
                               base64.b64encode(repr(payload).encode()) +
                               SECRET_KEY.encode())

    # jwt 토큰 생성
    jwt = base64.b64encode(repr(header).encode()).decode("UTF-8") + '.' + \
        base64.b64encode(repr(payload).encode()).decode("UTF-8") + '.' + \
        base64.b64encode(signature.hexdigest().encode()).decode()

    return Response({'session': {'email': userinfo.json()['response']['email'], 'jwt': jwt.replace('=', '')}}, status=status.HTTP_200_OK)


# user end
