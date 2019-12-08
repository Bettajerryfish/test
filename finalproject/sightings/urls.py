from django.urls import path
from django.conf.urls import url, include
from . import views

app_name='sightings'

urlpatterns = [

            path('', views.home, name = 'home'),
            path('add/', views.add, name = 'add'),
            path('stats/', views.stats, name = 'stats'),
            path('<unique_squirrel_id>/', views.update, name = "update"),

             ]
