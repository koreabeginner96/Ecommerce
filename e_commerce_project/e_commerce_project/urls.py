# 프로젝트 루트의 urls.py
from django.contrib import admin
from django.urls import path, include  # include 함수를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),           # 관리자 페이지
    path('shop/', include('shop.urls')),       # shop 앱의 URL을 포함
    # 여기에 다른 앱들의 URL 구성을 추가할 수 있다.
]
