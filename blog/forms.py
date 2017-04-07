from django import forms

from .models import Post, UserProfile

# Importa los usuarios de django.contrib.auth.models
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

# Formulario para los usuarios a agregar.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')  

# Formulario de los perfiles de usuario.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
