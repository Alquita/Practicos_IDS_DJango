from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    cursos = Curso.objects.all().order_by("-id")
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form,})

@login_required
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.activo = False
        curso.save()
        
        return redirect('cursos')
    return render(request, 'cursos/borrar_curso.html', {'curso': curso})