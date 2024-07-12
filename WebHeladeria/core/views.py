from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Clientes, CondicionIva
from .forms import ClienteCreationForm

from django.conf import settings # Para determinar si existe la foto del cliente en profile
import os # Para determinar si existe la foto del cliente en profile

def not_logged_in(user):
    return not user.is_authenticated


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = ClienteCreationForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')  # Redirige a la página principal u otra página de tu elección
        else:
            form = ClienteCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    else:
        return redirect('index')  # Redirige a la página principal u otra página de tu elección

@login_required
def profile(request):
    user = request.user
    
    cliente = Clientes.objects.get(username=user.username)
    condicion_iva = cliente.id_condicion_iva.condicion_iva
    
    foto_cliente_ruta = os.path.join(settings.MEDIA_ROOT, cliente.foto_cliente.name)
    if os.path.exists(foto_cliente_ruta):
        foto_cliente = cliente.foto_cliente.url
    else:
        foto_cliente = '/static/img/imagenes_clientes/default.png'

    context = {
        'usuario': cliente.username,
        'email': cliente.email,
        'nombre': cliente.first_name,
        'apellido': cliente.last_name,
        'direccion': cliente.direccion,
        'telefono': cliente.telefono,
        'foto_cliente': foto_cliente, #cliente.foto_cliente.url,
        'condicion_iva': condicion_iva,
    }
    
    return render(request, 'profile.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir al cliente a la página de inicio
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'

    else:
        error_message = ''

    return render(request, 'index.html', {'error_message': error_message})

def index(request):
    return render(request, 'index.html')


def salir(request):
    logout(request)
    return redirect('index')
