"""
URL configuration for rbac_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect
# users/urls.py

from users import views



# Simple root view for the home page
def home(request):
    return HttpResponse("Welcome to the RBAC Project!")

# Alternatively, redirect root URL to /api/users/
# def root_redirect(request):
#     return redirect('/api/users/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Existing user API routes
    path('', home, name='home'),  # Add this for the root URL
    path('tester/', views.tester, name='tester'),  # Ensure this path exists
    # path('', root_redirect, name='root_redirect'),  # Uncomment if you want redirection
]

