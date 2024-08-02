#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  #return HttpResponse("Hello Home Page!")
  return render(request, 'home.html')
  

def about(request):
  #return HttpResponse("My about Page!")
  return render(request, 'about.html')
