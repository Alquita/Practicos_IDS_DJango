from django.shortcuts import render, redirect

from .forms import AlumnoForm

# Create your views here.

def registrarse(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()

            return redirect('index')
    else:
        form = AlumnoForm()
    
    return render(request, 'registration/register.html', {'form': form})
