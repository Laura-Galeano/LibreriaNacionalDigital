from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import CustomUserCreationForm,UserEditForm
from .models import Usuario
from django.views import generic
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

def Inicio(request):
    return render(request,'Home.html')

#
#    return render(request,'editarperfil.html')

def Cambiarcontraseña(request):
    return render(request,'cambiarcontraseña.html')

def Datosfinancieros(request):
    return render(request,'datosfinancieros.html')

def Registrarse(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,usuario)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="editarperfil")
        data["form"]= formulario
    return render(request, 'registration/Registrarse.html', data)

class UserEditView(generic.UpdateView):
    model= Usuario
    form_class = UserEditForm
    template_name = 'editarperfil.html'
    succes_url = reverse_lazy('editarperfil')

    def get_object(self):
        return self.request.user




