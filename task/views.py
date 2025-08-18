from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Task Management System!<br> contact us at: <a href='/contact'>Contact</a>")

def contact(request):
    return HttpResponse("<h1 style='color:red'>This is contact page<h1/> <br> home page: <a href='/'>Home<a/>")

def show_task(request):
    return HttpResponse("This is the show task page!<br> <a href='/'>Home</a>")