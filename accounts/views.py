from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .forms import UserCreateForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators  import login_required

from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import UserCreateForm,UserProfileForm

def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {
                    'form': UserCreateForm(),
                    'error': 'Username already taken. Choose a new username.'
                })
        else:
            return render(request, 'signupaccount.html', {
                'form': form,
                'error': 'Passwords do not match' if 'password1' in form.errors else 'Please correct the error(s) below.'
            })

         
#add logout functionality
@login_required
def logoutaccount(request):
     #call logout and redirect to go back to the home page
     logout(request)
     return redirect('home')
def loginaccount(request):
     if request.method == 'GET':
          return render(request,'loginaccount.html', {'form':AuthenticationForm}) 
     
     else:
          user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
          if user is None:
               return render(request,'loginaccount.html', {'form':AuthenticationForm,'error': 'username and password do not match'}) 
          else:
               login(request,user)
               return redirect('home')
          
@login_required
def update_profile_image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Get or create UserProfile for the current user
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            # Update the profile image
            user_profile.image = form.cleaned_data['image']
            user_profile.save()
            return redirect('home')  # Redirect to the profile page after updating
    else:
        form = UserProfileForm()
    return render(request, 'update_profile_image.html', {'form': form})

             


