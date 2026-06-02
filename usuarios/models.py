from django.db import models
from django.contrib.auth.models import AbstractUser
from cursos.models import Curso

class Alumno(AbstractUser):
    cursos = models.ManyToManyField(
        Curso,
        default=None,
        blank=True,
        related_name='cursos',
    )
    foto_perfil = models.ImageField(upload_to='usuarios_fotos/', null=True, blank=True)
