from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.
def loginpage(request):
    return render(request = request,
		  template_name='main/login.html',
		  context = {"tutorials":Tutorial.objects.all})

def signup(request):
    return render(request = request,
		  template_name='main/signup.html',
		  context = {"tutorials":Tutorial.objects.all})

def homepage(request):
    return render(request = request,
		  template_name='main/home.html',
		  context = {"tutorials":Tutorial.objects.all})

def homeinpage(request):
    return render(request = request,
		  template_name='main/home_in.html',
		  context = {"tutorials":Tutorial.objects.all})

def profilepage(request):
    return render(request = request,
		  template_name='main/profile.html',
		  context = {"tutorials":Tutorial.objects.all})

