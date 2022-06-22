from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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