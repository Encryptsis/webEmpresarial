from django.shortcuts import render

# Create your views here.
from .models import Project

def portfolio(request):
    projects = Project.objects.all().order_by("-created")
    return render(request, "portfolio.html", {"projects": projects})

