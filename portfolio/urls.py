"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('project_details/', views.project_details, name='project_details'),
    path('404/', views.error_404, name='error_404'),
    path('smart-bin/', views.smart_bin, name='smart_bin'),
    path('weather-station/', views.weather_station, name='weather_station'),
    path('portfolio-website/', views.portfolio_website, name='portfolio_website'),
    path('networking-lab/', views.networking_lab, name='networking_lab'),
]
