from django.urls import path
from . import views

urlpatterns = [
    path('', views.planning_index, name='planning_index'),
]