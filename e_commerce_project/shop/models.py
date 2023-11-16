from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 카테고리 모델: 제품을 분류하기 위한 모델
class Category(models.Model):
    name = models.CharField(max_length=100)  # 카테고리 이름
    description = models.TextField()         # 카테고리 설명

    def __str__(self):
        return self.name  # 객체를 문자열로 표현할 때 카테고리 이름을 사용

# 제품 모델: 각각의 제품에 대한 정보를 저장
class Product(models.Model):
    name = models.CharField(max_length=100)  # 제품 이름
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 제품 가격
    description = models.TextField()         # 제품 설명
    stock = models.IntegerField()            # 제품 재고 수량
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 제품 카테고리 (Category 모델과의 외래 키 관계)

    def __str__(self):
        return self.name  # 객체를 문자열로 표현할 때 제품 이름을 사용

class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # 'Product'를 문자열로 참조
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # 항목이 장바구니에 추가된 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 항목이 마지막으로 업데이트된 날짜

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    @property
    def subtotal(self):
        return self.product.price * self.quantity  # 항목의 소계를 계산