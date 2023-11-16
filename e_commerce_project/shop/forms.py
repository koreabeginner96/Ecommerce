from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='유효한 이메일 주소를 입력하세요.')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("이미 존재하는 사용자 이름입니다.")
        return username
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

