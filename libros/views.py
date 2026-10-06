from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})


def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        fecha_publicacion = request.POST['fecha_publicacion']

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero,
            fecha_publicacion=fecha_publicacion
        )

        return redirect('lista_libros')

    return render(request, 'libros/agregar.html')


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.genero = request.POST['genero']
        libro.fecha_publicacion = request.POST['fecha_publicacion']

        libro.save()

        return redirect('lista_libros')

    return render(request, 'libros/editar.html', {'libro': libro})


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()

    return redirect('lista_libros')