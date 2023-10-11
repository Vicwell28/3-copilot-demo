from django.shortcuts import render
from .models import Libro

def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})