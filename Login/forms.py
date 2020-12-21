from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class DetailForm(forms.Form):
     name=forms.CharField(label='name',max_length=1000)
     mobile=forms.FloatField(label='mobile')
     password=forms.CharField(label='password',max_length=100)




class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    #full_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
