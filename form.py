from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User
from django import forms



# Create your models here.
#stroing usedata sign up
#class userregistration(UserCreationForm):
#	class meta:
#		model = User
#		fields = ['first_name', 'last_name', 'email', 'phone no.', 'gender', 'password1', 'password1']