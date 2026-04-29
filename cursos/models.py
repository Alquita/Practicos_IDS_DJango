from django.db import models

class Modalidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    actvo = models.BooleanField(default=True, null=True)


    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    precio = models.IntegerField()
    nivel = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    modalidad = models.ForeignKey(
        Modalidad, 
        on_delete=models.CASCADE, 
        related_name='cursos',
        null=True,
        blank=True,
        default=None
        )

    def __str__(self):
        return f'Soy el curso {self.nombre}'