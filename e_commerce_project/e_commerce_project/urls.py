# 프로젝트 루트의 urls.py
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include  # include 함수를 임포트
from shop import views
from shop.views import SignUpView
from shop.views import profile, update_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),           # 관리자 페이지
    path('shop/', include('shop.urls')),       # shop 앱의 URL을 포함
    # 여기에 다른 앱들의 URL 구성을 추가할 수 있다.
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/profile/', profile, name='profile'),  # 프로필 페이지 URL 설정
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),#URL은 Django의 기본 비밀번호 변경 뷰를 사용합니다.
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),#사용자가 비밀번호를 성공적으로 변경한 후에 표시되는 페이지를 위한 URL입니다.
    path('order/create/', views.order_create, name='order_create'),# 주문 생성 페이지 URL
    path('payment/process/', views.payment_process, name='payment_process'),# 결제 처리 뷰: 사용자가 결제를 진행하는 과정을 처리합니다.
    path('payment/done/', views.payment_done, name='payment_done'),# 결제 완료 뷰: 결제가 성공적으로 완료되었을 때 표시되는 페이지를 처리합니다.
    path('payment/canceled/', views.payment_canceled, name='payment_canceled'),# 결제 취소 뷰: 결제가 취소되었거나 실패했을 때 표시되는 페이지를 처리합니다.   
    path('cart/update/<int:product_id>/', update_cart, name='update_cart'),
]
