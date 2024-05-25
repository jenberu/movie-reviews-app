from django.shortcuts import render
from django.http import HttpResponse
def home(request):
 return HttpResponse('<h1>Welcome to Home Page</h1>')
# Create your views here.
def about(request):
 return HttpResponse('<h1>Welcome to About Page</h1>')