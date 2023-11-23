from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


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
#장바구니
class CartItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # 'Product'를 문자열로 참조
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)  # 항목이 장바구니에 추가된 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 항목이 마지막으로 업데이트된 날짜

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
#장바구니 total amount
    @staticmethod
    def get_cart_total(user):
        total = 0
        cart_items = CartItem.objects.filter(user=user)
        for item in cart_items:
            total += item.product.price * item.quantity
        return total

    @property
    def subtotal(self):
        return self.product.price * self.quantity  # 항목의 소계를 계산
#사용자 정보  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User 모델과 1:1 관계
    bio = models.TextField(max_length=500, blank=True)  # 사용자 소개
    birthday = models.DateField(null=True, blank=True)  # 생일 필드 추가
    gender = models.CharField(max_length=10, blank=True)  # 성별 필드 추가

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # 새로운 User 인스턴스가 생성될 때 UserProfile도 자동 생성

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 주문한 사용자
    created_at = models.DateTimeField(auto_now_add=True)  # 주문 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 주문 업데이트 시간
    paid = models.BooleanField(default=False)  # 결제 여부
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    PAYMENT_METHOD_CHOICES = [
        ('신용카드', '신용카드'),
        ('무통장 입금', '무통장 입금'),
    ]#결제방식
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='CC')

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)  # 해당 주문
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 주문한 제품
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 제품 가격
    quantity = models.PositiveIntegerField(default=1)  # 수량

    def __str__(self):
        return str(self.id)