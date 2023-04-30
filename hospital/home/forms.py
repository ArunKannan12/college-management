from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class stadm(ModelForm):
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    date_of_birth=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Date of birth','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter the email ID','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone number','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your address','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your city','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    state=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your state','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    pin=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your pin','style':'width:300px;height:200px;border-radius:10px;border:2px skyblue solid;'}))
    
    class Meta:
        model=admission
        fields=['firstname','lastname','date_of_birth','email','gender','phone','address','city','state','pin','courses_available','image']

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class Feedbackform(ModelForm):
    name=forms.CharField(required=True ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    feedback=forms.CharField(required=True ,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'type your feedback','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    class Meta:
        model=Feedback
        fields=['name','dept','feedback']