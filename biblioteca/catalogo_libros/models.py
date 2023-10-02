from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    anio = models.IntegerField()
    editorial = models.CharField(max_length=255)

def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title

def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)])