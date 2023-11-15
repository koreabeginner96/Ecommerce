from django.shortcuts import render
from .models import Product  # 모델 임포트

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()  # 데이터베이스에서 모든 제품을 조회
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)  # 특정 id의 제품을 조회
    return render(request, 'shop/product_detail.html', {'product': product})
