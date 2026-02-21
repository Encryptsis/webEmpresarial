from django.shortcuts import render

from .models import Project


def portfolio(request):
    projects = Project.objects.all().order_by("-created")
    return render(request, "portfolio.html", {"projects": projects})
