# Rest API Url 패턴 객체
from django.conf.urls import url
from django.urls import path

# 현재 페이지에서 views.py를 읽어온다.
from . import views

# 주소 뒤에 book를 붙이면 getRequest 함수의 리턴값이 호출된다.
urlpatterns = [
    path('users', views.user_list),
    path('users/<int:pk>', views.user_detail),
    path('users/<int:fromID>/followers', views.followers_list),
    path('users/<int:fromID>/followers/<int:toID>', views.followers_detail),
    path('login', views.user_login),
    path('session-check', views.session_refresh),
    path('sign-up', views.sign_up),
    path('user-delete', views.user_delete),
    path('bhour-store', views.bhour_find_by_store),
    path('menu-store', views.menu_find_by_store),
    path('review-store', views.review_find_by_store),
    path('review-user', views.review_find_by_user),
    path('store-name', views.store_find_by_name),
    path('check', views.oauth_code_google),
    path('check2', views.oauth_code_naver),
]
