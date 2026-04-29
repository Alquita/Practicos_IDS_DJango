from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso')
]
