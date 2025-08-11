from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mnblog/', include('mnblog.urls')),
    path('common/', include('common.urls')),
]
