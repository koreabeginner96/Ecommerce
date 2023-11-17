from django.contrib import admin
from .models import Category, Product
from .models import Order, OrderItem

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

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']  # 제품 검색을 위한 raw_id 필드

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid', 'created_at', 'updated_at']  # 관리자 목록에서 표시할 필드
    list_filter = ['paid', 'created_at', 'updated_at']  # 필터 옵션
    inlines = [OrderItemInline]  # 주문 항목을 같은 페이지에서 편집