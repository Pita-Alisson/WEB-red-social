from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PerfilUsuario, Usuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['foto_perfil', 'foto_portada', 'biografia']  # Incluye todos los campos relevantes
        
class RegistroUsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombres', 'nombre_usuario', 'email', 'contrasena']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['biografia', 'foto_perfil', 'foto_portada']


from django import forms
from .models import Grupo, PublicacionGrupo

class CrearGrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'descripcion']

class PublicacionGrupoForm(forms.ModelForm):
    class Meta:
        model = PublicacionGrupo
        fields = ['contenido', 'imagen']







#class FormCreationUsuario (UserCreationForm):
 #   class Meta(UserCreationForm.Meta):
  #      model = UsuarioPersonalizado
   #     fields = ('namee', 'user', 'email','password')
        
#class FormActualizarUsuario(UserChangeForm):
 #   class Meta(UserChangeForm.Meta):
  #      model = UsuarioPersonalizado
   #     fields = ('namee', 'user', 'email')