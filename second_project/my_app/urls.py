from django.urls import path
from . import views

urlpatterns = [
    path('', views.Developers_Page, name='developers_list'),
    path('<str:username>/', views.Developer_CV, name='developers_cv'),
]