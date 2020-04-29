from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Review
from .serializers import ReviewSerializer

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


@api_view(['POST'])
def update_default_score_by_click(request, store_id, user_id):
    reviews = queryset.filter(user_id=user_id, store_id=store_id)
    if reviews:
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        serializer = ReviewSerializer(
            data={"content": "auto-generated", "score": 3})
        if serializer.is_valid(raise_exception=True):
            serializer.save(store_id=store_id, user_id=user_id)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
