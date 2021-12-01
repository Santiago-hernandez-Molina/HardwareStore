from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Perfil

from .forms import SignUpForm

from django.contrib.auth.views import LoginView

class SignIn(LoginView):
    template_name = 'perfiles/login.html'

def logout_v(request):
    logout(request)
    return redirect('login')

class SignUp(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/products')