from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="회원가입 확인에 필요한 이메일입니다.")
    nickname = forms.CharField(max_length=30, help_text="닉네임을 입력하세요.")

    class Meta:
        model = User
        fields = ("username", "nickname", "email", "password1", "password2")
        labels = {
            "username": "사용자 아이디",
            "nickname": "닉네임",
            "email": "이메일",
            "password1": "비밀번호",
            "password2": "비밀번호 확인",
        }

    def clean_email(self):
        email = self.cleaned_data.get("email", "").lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 사용 중인 이메일입니다.")
        return email

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname", "").strip()
        if Profile.objects.filter(nickname__iexact=nickname).exists():
            raise forms.ValidationError("이미 사용 중인 닉네임입니다.")
        return nickname

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"].lower()
        if commit:
            user.save()
            Profile.objects.create(user=user, nickname=self.cleaned_data["nickname"].strip())
        return user
