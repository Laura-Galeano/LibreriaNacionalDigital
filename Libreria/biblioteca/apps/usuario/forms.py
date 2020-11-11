from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','nombres','apellidos','email','Cedula','Fecha_nacimiento',
        'temas_preferidos','password1','password2','suscripcion']
        
        widgets = {
            'Fecha_nacimiento': forms.DateInput(
                format='%m/%d/%Y',
                attrs = {
                    'class': 'datepicker',
                    'autocomplete': 'off',
                    'id': 'fecha_nacimiento',
                    'required': 'required'
                }
            ),
            #'genero': forms.Select(
            #    attrs = {
            #        'id': 'genero',
            #        'required': 'required'
            #    }
            #),
            'suscripcion': forms.CheckboxInput(
                attrs = {
                    'class': '',
                    'id': 'noticias',
                    'required': 'required',
                }
            )
            
        }
class UserEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username','nombres','apellidos','email','Cedula','Fecha_nacimiento',
        'temas_preferidos','suscripcion']
        
        widgets = {
            'Fecha_nacimiento': forms.DateInput(
                format='%m/%d/%Y',
                attrs = {
                    'class': 'datepicker',
                    'autocomplete': 'off',
                    'id': 'fecha_nacimiento',
                    'required': 'required'
                }
            ),
            #'genero': forms.Select(
            #    attrs = {
            #        'id': 'genero',
            #        'required': 'required'
            #    }
            #),
            'suscripcion': forms.CheckboxInput(
                attrs = {
                    'class': '',
                    'id': 'noticias',
                    'required': 'required',
                }
            )
            
        }