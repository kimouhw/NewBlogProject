from django.urls import path
from . import views

urlpatterns = [
    path('connexion',views.connexion,name='connexion'),
    path('inscription',views.inscription,name='inscription'),
    path('deconnexion',views.deconnexion,name='deconnexion')
]