from django.contrib.auth.forms import UserCreationForm
from .models import Alumno

class AlumnoForm(UserCreationForm):
    class Meta():
        model = Alumno
        fields = UserCreationForm.Meta.fields + ('email', 'foto_perfil')