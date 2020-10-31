from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='accueil'),
    path('tutoriels/<int:id>/', views.listTutorials, name='tutoriels'),
    path('detail/<int:id>/', views.detailTutorial, name='detail-tutoriel'),
]