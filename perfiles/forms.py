from django import forms
from perfiles.models import Perfil

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["nombre_usuario", "email", "contraseña"]