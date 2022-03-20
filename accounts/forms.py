from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'reg_input', 'placeholder': 'Иван'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'reg_input', 'placeholder': 'Иванов'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'reg_input', 'placeholder': 'name.ac@yandex.ru'})
        self.fields['email'].required = True
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'reg_input', 'placeholder': 'admin'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'reg_input', 'id': 'user-password', 'placeholder':"Придумайте сложный пароль"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'reg_input', 'id': 'user-confirm-password', 'placeholder': 'Подтверждение пароля'})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact = email)
        if qs.exists():
            raise forms.ValidationError("Такая почта уже существует")
        return email
    
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if username in non_allowed_username:
    #         raise forms.ValidationError("Вы или выбрали зарезервированное имя, или обидели меня. Одно из двух, надеюсь первое.")
    #     return username


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()