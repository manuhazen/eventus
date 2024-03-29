from django import forms

from users.models import User


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa un nombre de usuario'}),
            'password' : forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Ingresa una clave segura'}),
            'email': forms.TextInput(attrs={'type' : 'email', 'class': 'form-control', 'placeholder': 'Ingresa una cuenta de correo electronico'})
        }

class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=30, widget= forms.TextInput
                        (attrs={
                           'class': 'form-control',
                            'placeholder': 'Ingresa tu username'
                        }))
    password = forms.CharField(max_length=30, widget= forms.TextInput(
                        attrs={'type' : 'password',
                               'class': 'form-control',
                               'placeholder': 'Ingresa un password'
                               }))