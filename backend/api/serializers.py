from .models import BHour, Menu, Review, Store, User
from rest_framework import serializers


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        # fields = '__all__'
        fields = ('id', 'followers', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        # fields = '__all__'
        fields = ('id', 'name', 'nick_name', 'gender', 'birthday',
                  'profile_picture', 'cover_picture', 'born_year')


class BhourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BHour
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
