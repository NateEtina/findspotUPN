from django.urls import path
from . import views

app_name = 'mapping'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('buildings/', views.showBuilding, name='tobuilding'),
    path('bureaux/', views.showBureau, name='tobureau'),
    path('locals/', views.showLocal, name='tolocal'),
    path('spaces/', views.showSpace, name='tospace'),
]