from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
from .models import Order


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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birthday', 'gender']  # 예시 필드

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': '이름'}),
            'last_name': forms.TextInput(attrs={'placeholder': '성'}),
            'email': forms.EmailInput(attrs={'placeholder': '이메일'}),
            'address': forms.TextInput(attrs={'placeholder': '주소'}),
            'postal_code': forms.TextInput(attrs={'placeholder': '우편번호'}),
            'city': forms.TextInput(attrs={'placeholder': '도시'}),
        }