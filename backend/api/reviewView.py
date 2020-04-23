from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Review

queryset = Review.objects.all()

@api_view(['GET'])
def detail(request, id=None, ):
    result = queryset.filter(id__exact=id)
    return Response({'result': result.values()}, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list(request, score=None, id=None):
    if score is not None:
        condition = request.GET.get('condition')
        if condition is not None and condition.lower() == 'down':
            result = queryset.filter(score__lte=score)
            return Response({"result": result.values()}, status=status.HTTP_200_OK)
        result = queryset.filter(score__gte=score)
        return Response({"result": result.values()}, status=status.HTTP_200_OK)
    elif id != 0:
        result = queryset.filter(user_id__exact=id)
        return Response({'result': result.values()}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)