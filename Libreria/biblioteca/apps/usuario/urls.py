from django.urls import path
from .views import Registrarse,Inicio,Cambiarcontraseña,Datosfinancieros,UserEditView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('registrarse/',Registrarse, name='registrarse'),
    path('editarperfil/',UserEditView.as_view(), name='editarperfil'),
    path('inicio/',Inicio, name='inicio'),
    path('cambiarcontraseña/',Cambiarcontraseña, name='cambiarcontraseña'),
    path('datosfinancieros/',Datosfinancieros, name='datosfinancieros'),
]