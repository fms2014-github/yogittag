from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Store, BHour, Menu, Review
from .serializers import StoreSerializer

queryset = Store.objects.all()

@api_view(['GET'])
def detail(requset, id=None):
    # id = requset.GET.get('id')
    print(id)
    result = queryset.filter(id__exact=id)
    return Response({'result': result.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def store_find_by_name(request, name=None):
    # 검색 요청 정보 가져오기
    result_search = Store.objects.filter(store_name__contains=name)
    return Response({"result": result_search.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def bhour_find_by_store(request, id=None):
    result = BHour.objects.filter(store_id__exact=id)
    return Response({"result": result.values()}, status.HTTP_200_OK)


@api_view(['GET'])
def menu_find_by_store(request, id=None):
    result = Menu.objects.filter(store_id__exact=id)
    return Response({"result": result.values()}, status.HTTP_200_OK)

@api_view(['GET'])
def review_find_by_store(request, id=None):
    result = Review.objects.filter(store_id__exact=id)
    print(result)
    return Response({"result": result.values()}, status.HTTP_200_OK)