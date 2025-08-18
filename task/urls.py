from django.urls import path
from django.shortcuts import render
from task.views import show_task


urlpatterns = [
    path('show-task/', show_task)
]
