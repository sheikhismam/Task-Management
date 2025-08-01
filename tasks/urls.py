from django.contrib import admin
from django.urls import path
from tasks.views import show_task, show_specific_task

urlpatterns = [
    path('', show_task),
    path('show-task/<int:id>/', show_specific_task)
]
