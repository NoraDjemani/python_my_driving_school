from django.urls import path
from . import views

urlpatterns = [
    path('', views.forfait_index, name='forfait_index'),
]