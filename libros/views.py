from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    mensaje = ''

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')

        user = authenticate(request, username=usuario, password=clave)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(request, 'login/login.html', {'mensaje': mensaje})


@login_required
def inicio(request):
    return render(request, 'inicio.html')


def salir(request):
    logout(request)
    return redirect('login')