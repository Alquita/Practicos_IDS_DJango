from django.shortcuts import render, get_list_or_404, redirect
from .models import Curso
from .forms import CursoForm

def inicio(request):
    return render(request, 'cursos/index.html')

def cursos(request):
    cursos = Curso.objects.all().order_by("-id")
    return render(request, 'cursos/cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

def editar_curso(request, curso_id):
    curso = get_list_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form,})


def eliminar_curso(request, curso_id):
    curso = get_list_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.activo = False
        curso.save()
        
        return redirect('cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})