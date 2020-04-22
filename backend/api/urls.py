 # Rest API Url 패턴 객체
from django.conf.urls import url
from django.urls import path

# 현재 페이지에서 views.py를 읽어온다.
from . import views, storeView, menuView, reviewView


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
    path('review/<int:id>', reviewView.detail),
    path('review/<int:score>/score', reviewView.review_list),
    path('user/<int:user>/review', reviewView.review_list),
    path('menu/<int:id>', menuView.detail),
    path('menu/<str:name>', menuView.menu_list_by_name),
    path('menu/<int:price>/price', menuView.menu_list_by_price),
    path('store/<int:id>', storeView.detail),
    path('store/<str:name>', storeView.store_find_by_name),
    path('store/<int:id>/menu', storeView.menu_find_by_store),
    path('store/<int:id>/bhour', storeView.bhour_find_by_store),
    path('store/<int:id>/review', storeView.review_find_by_store),
    path('check', views.oauth_code_google),
    path('check2', views.oauth_code_naver),
]