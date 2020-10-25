from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutoriels/<int:id>/', views.listTutorials, name='tutoriels'),
]