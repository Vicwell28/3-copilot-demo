from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
 path('', views.index, name='index'),
 path('crear/', views.crear_libro, name='crear_libro'),
 path('editar/<int:id>/', views.editar_libro, name='editar_libro'),
 path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]