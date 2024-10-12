from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map', views.map, name='map'),
    path('greenwaste', views.greenwaste, name='greenwaste'),
    path('find-container/', views.find_container, name='find_container'),
    path('apie', views.apie, name='apie'),
]
