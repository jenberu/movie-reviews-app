from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators  import login_required


def signupaccount(request):
    if request.method=='GET':
         return render(request, 'signupaccount.html', {'form':UserCreateForm})
    else:
         if request.POST['password1'] == request.POST['password2']:
              try:
                  user=User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
                  user.save()
              #automatically log them in and redirect them to the home page.
                  login(request,user)
                  return redirect('home')
                  #Checking whether passwords do not match
              except IntegrityError:
                   return render(request,'signupaccount.html',{'form':UserCreateForm ,'error':'Username already taken. Choosse new username'})
         else:
              return render(request, 'signupaccount.html',{'form':UserCreateForm ,'error':'passwords do not match'})
         
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
             


