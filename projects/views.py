from django.shortcuts import render
from .models import Project

# Create your views here.


def list_projects(request):
    project_list = Project.objects.all()
    context = {"project_list": project_list}

    return render(request, "projects/list.html", context)
