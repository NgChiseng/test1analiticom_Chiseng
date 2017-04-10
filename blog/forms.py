from django import forms

from .models import Post, UserProfile, User

# Used for import the Django Users of contrib.auth.models
#from django.contrib.auth.models import User

# Used for importing structures that configure the form attributes.
import re
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

# Form used in the register.
class UserForm(forms.ModelForm):

	# Form validation variables
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Confirm Password"))
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))

    # Function that evaluate if an username exist yet in database to avoid repetitions.
	#
	# @date [10/04/2017]
	#
	# @author [Chiseng Ng]
	#
	# @param [Post] self Object that invoque this method.
	#
	# @returns [NONE]
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
 	# Function that evaluate if the password match with the confirm password.
	#
	# @date [10/04/2017]
	#
	# @author [Chiseng Ng]
	#
	# @param [Post] self Object that invoque this method.
	#
	# @returns [NONE]
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    # Definition of form validation variables
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        }

# Form used to update user profile in the register.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

# Form used to log in fields.
class UserLogin(forms.ModelForm):
	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	# Definition of form validation variables
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
			'password': forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
		}
	