from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re


class SignUpForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            print(1)
            raise forms.ValidationError('поле имя не должно быть менее 3 символов')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if 'spam' in email:
            raise forms.ValidationError('span нельзя кароч')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')

        if len(password1) < 8:
            raise forms.ValidationError('Длина пароля должна быть не менее 8 символов')

        if len(re.findall(r'[A-Z]', password1)) < 2:
            raise forms.ValidationError('Пароль должен содержать минимум 2 заглавные буквы')

        if len(re.findall(r'\d', password1)) < 2:
            raise forms.ValidationError('Пароль должен содержать минимум 2 цифры')

        return password2

    class Meta:
        model = User
        fields = 'username', 'email', 'password1', 'password2'


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )

