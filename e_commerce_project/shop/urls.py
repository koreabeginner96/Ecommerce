# shop 앱의 urls.py
from django.urls import path
from . import views  # 현재 앱의 뷰를 임포트
urlpatterns = [
    path('', views.index, name='index'),                     # 메인 페이지
    path('products/', views.product_list, name='product_list'),  # 제품 목록 페이지
    path('products/<int:id>/', views.product_detail, name='product_detail'),  # 제품 상세 페이지
]
