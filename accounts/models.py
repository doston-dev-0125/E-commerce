from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class UserCreateForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email',error_messages={'exists':'This  Already Exists'})
    
    class Meta:
     model=User
     fields=('username','email','password1','password2')
   
    def __init__(self, *args,**kwargs):
      super(UserCreateForm,self).__init__(*args,**kwargs)
      self.fields['username'].widget.attrs['placeholder']='Username'
      self.fields['email'].widget.attrs['placeholder']='Email'
      self.fields['password1'].widget.attrs['placeholder']='Password'
      self.fields['password2'].widget.attrs['placeholder']='Confrim Password'
      
    def save(self , commit=True):
     user=super(UserCreateForm,self).save(commit=False)
     user.email=self.cleaned_data['email']
     if commit:
        user.save()
     return user
    
    def clean_email(self):
       if User.objects.filter(email=self.cleaned_data['email']).exists():
          raise forms.ValidationError(self.fields['email'].error_message['exists'])
       return self.cleaned_data['email']
    
    
class Contact(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      subject=models.CharField(max_length=100)
      message=models.TextField()

      def __str__(self) -> str:
         return self.name
