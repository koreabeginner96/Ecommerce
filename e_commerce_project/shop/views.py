from django.shortcuts import render
from .models import Product  # 모델 임포트
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm  # 커스텀 회원가입 폼 사용
from django.shortcuts import redirect, get_object_or_404
from .models import Product, CartItem


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

def add_to_cart(request, product_id):
    """
    사용자가 선택한 제품과 수량을 장바구니에 추가합니다.
    """
    product = get_object_or_404(Product, id=product_id)  # 선택한 제품을 가져옵니다.
    # 요청에서 수량을 가져옵니다. 기본값은 1입니다.
    quantity = int(request.POST.get('quantity', 1))
    # 장바구니 항목을 가져오거나 새로 생성합니다.
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if created:
        cart_item.quantity = quantity  # 새 항목이면 사용자가 선택한 수량을 설정합니다.
    else:
        cart_item.quantity += quantity  # 기존 항목이면 수량을 추가합니다.
    cart_item.save()  # 장바구니 항목을 저장합니다.
    return redirect('cart_detail')  # 장바구니 상세 페이지로 리디렉션합니다.

def cart_detail(request):
    """
    사용자의 장바구니 내용을 보여주는 뷰입니다.
    현재 로그인한 사용자의 장바구니 항목들을 조회하여 표시합니다.
    """
    cart_items = CartItem.objects.filter(user=request.user)  # 현재 사용자의 장바구니 항목을 가져옵니다.
    # 각 장바구니 항목에 대한 총 가격 계산
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items})