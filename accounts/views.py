from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import UserCreateForm,Contact

def signup(request):
 if request.method == 'POST':
  form=UserCreateForm(request.POST)
  if form.is_valid():
   new_user=form.save()
   new_user=authenticate (
    username=form.cleaned_data['username'],
    password=form.cleaned_data['password1'],
   )
   login(request,new_user)
   return redirect('index')
 else:
    form = UserCreateForm()
 
 context = {
  'form':form,
 }
  
 return render(request,'registration/signup.html',context)

def contact_us(request):
   if request.method == "POST":
      contact = Contact  (
         name=request.POST.get('name'),
         email=request.POST.get('email'),
         subject=request.POST.get('subject'),
         message=request.POST.get('message'),
      )
      contact.save()
   
   return render(request,'contact.html')