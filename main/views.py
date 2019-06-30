from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.
def homepage(request):
    return render(request = request,
		  template_name='main/login.html',
		  context = {"tutorials":Tutorial.objects.all})

def signup(request):
    return render(request = request,
                  template_name = "main/home.html",
                  context={})

def login(request):
    return render(request = request,
                  template_name = "main/login.html",
                  context={})

def upload(request):
    return render(request = request,
                  template_name = "main/upload.html",
                  context={})
