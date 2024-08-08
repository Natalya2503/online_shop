from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Имя пользователя',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'})
    )
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'})
    )

    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
    
# ----------------------------------------------------
                                         
class RegisterUserForm(UserCreationForm):
   
    username = forms.CharField(
        label = 'Имя пользователя',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя ",
            }
        )
    )
    last_name = forms.CharField(
        label = 'Имя',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию ",
            }
        )
    )
     
    email = forms.CharField(
        label = 'Email',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
            }
        )
    )
    phone_number = forms.CharField(
        label = 'Телефон',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш телефон",
            }
        )
    )
    password1 = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        label = 'Повтор пароля',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Поддтвердите ваш пароль",
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'last_name', 'email', 'phone_number', 'password1', 'password2'] 


#  ------------------------------------------------    

class ProfileForm(UserChangeForm):
    
    username = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Номер телефона",
            }
        )
    )
    email = forms.CharField(
        disabled=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
                
            }
        ),
    )

    class Meta:
        model = get_user_model() 
        fields = ['username', 'last_name', 'phone_number', 'email']                              
   
    