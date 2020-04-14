from .models import bhour, menu, review, store, user
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class BhourSerializer(serializers.ModelSerializer):
    class Meta:
        model = bhour
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


