from django.urls import path
from . import views

app_name = 'mnblog'

urlpatterns = [
    path('', views.home, name='home'),  # http://127.0.0.1:8000/
    path('post/<slug:slug>/', views.post_detail, name='detail'),
]
