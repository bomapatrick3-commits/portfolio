from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')
    
def project_details(request):
    return render(request, 'project_details.html')


def smart_bin(request):
    return render(request, "smart-bin.html")


def weather_station(request):
    return render(request, "weather-station.html")


def portfolio_website(request):
    return render(request, "portfolio-website.html")


def networking_lab(request):
    return render(request, "networking-lab.html")

def error_404(request, exception=None):
        return render(request, '404.html', status=404)