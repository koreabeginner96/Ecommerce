from django.contrib import admin
from .models import Category, Product

# Category 모델을 관리자 페이지에 등록
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # 관리자 페이지에서 보여줄 필드

# Product 모델을 관리자 페이지에 등록
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')  # 관리자 페이지에서 보여줄 필드
    list_filter = ('category',)  # 카테고리별로 필터링할 수 있게 설정
    search_fields = ('name', 'description',)  # 이름과 설명으로 검색 가능
