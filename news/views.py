from django.shortcuts import render
from django.http import HttpResponse
from .models import News
def news(request):
    #e displaying the most recent news first.
    #SELECT * FROM News ORDER BY date DESC;
    newss=News.objects.all().order_by('-date')

    return render(request,'news.html',{'newss':newss})


# Create your views here.
