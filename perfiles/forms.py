from django import forms
from perfiles.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nombre_usuario", "email", "contraseña"]