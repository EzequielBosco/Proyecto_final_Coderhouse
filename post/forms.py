from django.forms import ModelForm
from post.models import Comentarios

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nombre', 'correo', 'mensaje', 'activo')
