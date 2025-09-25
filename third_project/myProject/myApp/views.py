from django.shortcuts import render, HttpResponse, redirect
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm

def developers_list(request):
    myDev = Developer.objects.all()
    
    if not myDev:
        return HttpResponse("No Developers!")
    else:
        return render(request, "developers_list.html", {'devs': myDev})
    
def projects_list(request):
    myProject = Project.objects.all()

    if not myProject:
        return HttpResponse("No Projects!")
    else:
        return render(request, "projects_list.html", {'projects': myProject})
    
def create_developer(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dev_list")
        
    else:
        form = DeveloperForm()

    return render(request, "create_developer.html", {'form': form})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dev_list")
    else:
        form = ProjectForm()

    return render(request, "create_project.html", {'form': form})