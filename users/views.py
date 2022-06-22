from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.
def profile(request):
    
    current_user = request.user
    
    if request.method == 'POST':
      
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if profile_form.is_valid:
         
            profile_form.save()
           
            return redirect('dashboard/landing')
        
        else:
        
            profile_form = ProfileUpdateForm(instance=request.user.profile)
       
    
    return render(request, 'users/profile.html')
   

def register(request):
      #put a check in place
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            return redirect('login')
    else:
        form = UserCreationForm(request.POST)
    return render(request,'users/register.html',{'form':form})  
