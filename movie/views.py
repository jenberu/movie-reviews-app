from django.shortcuts import render
from django.http import HttpResponse
def home(request):
 #get the input value from  default GET method form
 searchTerm=request.GET.get('searchMovie')
 return render(request, 'home.html', {'searchTerm':searchTerm}
)
# Create your views here.
def about(request):
 return HttpResponse('<h1>Welcome to About Page</h1>')
def signup(request):
 email = request.GET.get('email')
 return render(request, 'signup.html', {'email':email})