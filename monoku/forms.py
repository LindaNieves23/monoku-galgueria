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
    def __init__(self,*args,**kwargs):
        super(PersonaForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'

            })


class GalgueriaForm(forms.ModelForm):

    class Meta:
        model = Galguerias
        fields = ('nombre_producto', 'tipo', 'fecha_vencimiento', 'cantidad_producto')
    def __init__(self,*args,**kwargs):
        super(GalgueriaForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'

            })


class PreferenciaForm(forms.ModelForm):

    class Meta:
        model = Preferecias_galguerias
        fields = ('persona', 'producto', 'cantidad_consumido')
    def __init__(self,*args,**kwargs):
        super(PreferenciaForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'

            })


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
    def __init__(self,*args,**kwargs):
        super(PreferenciaForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'

            })


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    def __init__(self,*args,**kwargs):
        super(PreferenciaForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'

            })
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
