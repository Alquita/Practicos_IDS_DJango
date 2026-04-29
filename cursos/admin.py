from django.contrib import admin
from .models import Curso, Modalidad

# Register your models here.

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'duracion', 'precio', 'nivel', 'modalidad', 'activo')
    list_filter = ('modalidad', 'activo',)
    search_fields = ('nombre', )

admin.site.register(Modalidad)
