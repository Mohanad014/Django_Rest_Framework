from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('product/<int:id>/', ProductViewByID.as_view()),  
    path('category/', CategoryView.as_view()),
    path('category/<int:id>/', CategoryViewByID.as_view()),
]
