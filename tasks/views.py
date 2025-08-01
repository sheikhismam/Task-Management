from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the Task Mangement System')
def show_task(request):
    return HttpResponse('This is our tasks page')