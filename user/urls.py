from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('', views.UserCreate.as_view()),
    path('login/', views.UserView.as_view()),
]