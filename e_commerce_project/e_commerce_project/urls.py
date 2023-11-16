# 프로젝트 루트의 urls.py
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include  # include 함수를 임포트
from shop import views
from shop.views import SignUpView

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
]
