from django.db import models

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
