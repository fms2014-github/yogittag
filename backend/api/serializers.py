from .models import BHour, Menu, Review, Store, User, FavoriteList, FavoriteStore
from rest_framework import serializers
from rest_framework.parsers import JSONParser


class FollowSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField('get_id')
    followers = serializers.SerializerMethodField('get_followers')

    class Meta:
        model = User
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        # fields = '__all__'
        fields = ('id', 'followers')

    def get_id(self, obj):
        print("obj id : ", obj.id)
        return str(obj.id)

    def get_followers(self, obj):
        # 여기서 obj가 user 객체 입니다.
        # 밑에 followers를 추출하는 알고리즘을 구현해주세요.
        ret = []

        followers = obj.followers.all()
        for follower in followers:
            ret.append({"id": follower.id})
        return ret


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        # fields = '__all__'
        fields = ('id', 'name', 'nick_name', 'gender', 'birthday',
                  'profile_picture', 'cover_picture', 'born_year')


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = '__all__'


class FavoriteStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteStore
        fields = '__all__'


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
        # fields = '__all__'
        fields = ('id', 'score', 'content', 'store_id', 'user_id',)


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        # 직렬화 시킬 컬럼명, 다른 의미로 주고 받을 데이터 명시
        fields = '__all__'
