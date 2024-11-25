from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_team, name='add_team'),
    path('view/', views.view_teams, name='view_teams'),
]

path('set_cookie/', views.set_cookie, name='set_cookie'),
path('get_cookie/', views.get_cookie, name='get_cookie'),
