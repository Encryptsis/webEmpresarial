from django.shortcuts import render

# Create your views here.
from .models import Project

def portfolio(request):
    projects = Project.objects.all().order_by("-updated_at", "-created")
    return render(request, "portfolio/portfolio.html", {"projects": projects})

