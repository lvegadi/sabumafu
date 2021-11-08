from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    #firts_name = forms.CharField(label='Nombre', widget=forms.TextInput, required=True )
    #last_name = forms.CharField(label='Apellido', widget=forms.TextInput, required=True)
    #email = forms.EmailField()
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)
    #password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }
