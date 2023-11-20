# shop 앱의 urls.py
from django.urls import path
from .views import add_to_cart, cart_detail
from . import views  # 현재 앱의 뷰를 임포트

urlpatterns = [
    path('', views.index, name='index'),                     # 메인 페이지
    path('products/', views.product_list, name='product_list'),  # 제품 목록 페이지
    path('products/<int:id>/', views.product_detail, name='product_detail'),  # 제품 상세 페이지
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),#제품 추가하는 view
    path('cart_detail/', cart_detail, name='cart_detail'),# 상세 페이지 보여주는 view
    
]   