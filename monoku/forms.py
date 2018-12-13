from django import forms
from .models import Personas
from .models import Galguerias
from .models import Preferecias_galguerias
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Personas
        fields = ('nombre_persona', 'edad', 'cargo')


class GalgueriaForm(forms.ModelForm):

    class Meta:
        model = Galguerias
        fields = ('nombre_producto', 'tipo', 'fecha_vencimiento', 'cantidad_producto')


class PreferenciaForm(forms.ModelForm):

    class Meta:
        model = Preferecias_galguerias
        fields = ('persona', 'producto', 'cantidad_consumido')


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
