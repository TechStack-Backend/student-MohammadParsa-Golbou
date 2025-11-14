from django.urls import path
from django.shortcuts import redirect
from .views import (
    DeveloperListView, DeveloperDetailView, DeveloperCreateView, DeveloperUpdateView, DeveloperDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
)

urlpatterns = [
    path('developers/', DeveloperListView.as_view(), name='developer_list'),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'),
    path('developers/add/', DeveloperCreateView.as_view(), name='developer_add'),
    path('developers/<int:pk>/edit/', DeveloperUpdateView.as_view(), name='developer_edit'),
    path('developers/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer_delete'),

    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]