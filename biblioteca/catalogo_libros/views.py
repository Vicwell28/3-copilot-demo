from django.shortcuts import render,HttpResponse, redirect
from .models import Libro

def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})
##Acciones del crud
def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        editorial = request.POST['editorial']
        anio = request.POST['anio']
        libro = Libro(titulo=titulo, descripcion=descripcion, anio=anio,editorial=editorial)
        libro.save()
        return redirect('index')
    else:
        return render(request, 'crear.html')

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.descripcion = request.POST['descripcion']
        libro.anio = request.POST['anio']
        libro.editorial = request.POST['editorial']
        libro.save()
        return redirect('index')
    else:
        return render(request, 'editar.html', {'libro': libro})

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('index')