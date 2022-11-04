from django import forms
from perfiles.models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["nombre_usuario", "email", "contraseña"]