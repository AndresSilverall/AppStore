
from django.urls import path
from . import views

urlpatterns = [
    path('Api/', views.api_movie, name="Api"),
    
]
