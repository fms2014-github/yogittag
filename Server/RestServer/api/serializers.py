from .models import Bhour, Menu, Review, Store, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class BhourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bhour
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'


