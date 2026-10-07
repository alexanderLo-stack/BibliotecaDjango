from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    mensaje = ''

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        user = authenticate(
            request,
            username=usuario,
            password=clave
        )

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(
        request,
        'login/login.html',
        {'mensaje': mensaje}
    )


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(
        request,
        'login/registro.html',
        {'form': form}
    )


@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def agregar_libro(request):
    return render(request, 'libros/agregar.html')


def salir(request):
    logout(request)
    return redirect('login')