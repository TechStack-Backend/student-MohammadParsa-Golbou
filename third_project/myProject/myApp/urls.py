from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('developers/', views.developers_list, name = "dev_list"),
    path('projects/', views.projects_list, name = "project_list"),
    path('developers/new', views.create_developer, name = "create_dev"),
    path('projects/new', views.create_project, name = "create_project"),
    path('', lambda request: redirect("dev_list")),
]