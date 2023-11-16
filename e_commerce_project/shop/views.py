from django.shortcuts import render
from .models import Product  # 모델 임포트
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm  # 커스텀 회원가입 폼 사용

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # 커스텀 회원가입 폼 지정
    success_url = reverse_lazy('login')  # 회원가입 성공 후 리디렉션할 URL
    template_name = 'signup.html'        # 사용할 템플릿 지정

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()  # 데이터베이스에서 모든 제품을 조회
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)  # 특정 id의 제품을 조회
    return render(request, 'shop/product_detail.html', {'product': product})

def home(request):
    return render(request, 'home.html')  # 'home.html'은 이 view에 해당하는 템플릿 파일입니다.