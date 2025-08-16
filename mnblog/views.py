# mnblog/views.py (최종)

from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.contrib.auth.decorators import login_required  # 로그인 제한이 필요하면 사용

# 홈 화면 (목록)
# @login_required(login_url='/common/login/')  # 로그인 후에만 보이게 하려면 주석 해제
def home(request):
    posts = Post.objects.all()  # DB에서 모든 게시물 불러오기
    return render(request, 'mnblog/home.html', {'posts': posts})

# 게시물 상세 페이지
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'mnblog/detail.html', {'post': post})
