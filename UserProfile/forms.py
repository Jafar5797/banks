from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 
User = get_user_model()
# settings.AUTH_USER_MODEL
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
	
	name = forms.CharField(max_length=30,label=mark_safe("<strong> Name  </strong>"), required=True, widget=forms.TextInput(attrs={'placeholder': 'please enter full name'}))
	email = forms.EmailField(label=mark_safe("<strong> Email (will be used as Username) </strong>"),max_length=254,required=True, widget=forms.EmailInput(attrs={'placeholder': 'enter a valid email address'}))
	password1 = forms.CharField(label=mark_safe("<strong> Choose Password </strong>"),widget=forms.PasswordInput(attrs={'placeholder': 'please enter password'}))
	password2 = forms.CharField(label=mark_safe("<strong> Confirm Password </strong>"),widget=forms.PasswordInput(attrs={'placeholder': 'please confirm password'}))

	class Meta(UserCreationForm):
		model = User
		fields = ['name','email',
		'password1','password2',]



