from django.urls import path
from tasks.views import show_task, show_specific_tasks

urlpatterns = [
    path('show-task/', show_task),
    path('show-task/<int:id>/', show_specific_tasks)
]