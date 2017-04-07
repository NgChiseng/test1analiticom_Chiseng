from django import forms

from .models import Post, UserProfile

# Used for import the Django Users of contrib.auth.models
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

# Form used in the register.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password', 'email',)  

# Form used to update user profile in the register.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
