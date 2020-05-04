from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Menu

queryset = Menu.objects.all()


@api_view(['GET'])
def detail(request, id=None):
    print(id)
    result = queryset.filter(id__exact=id)
    return Response({'result': result.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def menu_list_by_name(request, name=None):
    result = queryset.filter(menu_name__contains=name)
    return Response({"result": result.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def menu_list_by_price(request, price=None):
    condition = request.GET.get('condition')
    if condition is not None and condition.lower() == 'up':
        result = queryset.filter(menu_name__gte=price)
        return Response({"result": result.values()}, status=status.HTTP_200_OK)
    result = queryset.filter(menu_name__lte=price).filter(menu_name__gt=0)
    return Response({"result": result.values()}, status=status.HTTP_200_OK)