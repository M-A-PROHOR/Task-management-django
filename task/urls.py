from django.urls import path
from django.shortcuts import render
from task.views import manager_dashboard, user_dashboard


urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard)
]
