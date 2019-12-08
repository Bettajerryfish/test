from django.urls import path

from . import views

urlpatterns = [
    path('', views.squirrel_map, name='squirrel_map'),
]
