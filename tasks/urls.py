from django.urls import path

from tasks.views import create_task

app_name = 'tasks'
urlpatterns = [
    path('task_creation/', create_task, name='task_creation'),
]
