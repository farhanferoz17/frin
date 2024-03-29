"""mysiten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main' # here for namespacing of urls

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signuppage'),
    path('login/', views.loginpage, name='loginpage'),
    path('homein/', views.homeinpage, name='homeinpage'),
    path('profile/', views.profilepage, name='profilepage'),
]
