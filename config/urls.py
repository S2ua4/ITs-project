from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mnblog.urls')),      # 루트가 mnblog로 연결
    path('common/', include('common.urls')),
]
