from django.urls import path
from . import views

app_name = 'mnblog'

urlpatterns = [
    path('', views.home, name='home'),  # http://127.0.0.1:8000/
    path('post/create/', views.post_create, name='post_create'), # 이 부분이 글쓰기 페이지 URL,
    # <str:slug>는 한글을 포함한 대부분의 문자를 허용합니다.
    path('post/<str:slug>/', views.post_detail, name='detail'),

]
