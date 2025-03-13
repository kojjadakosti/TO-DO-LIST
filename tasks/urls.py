from django.urls import path

from tasks.views import create_task, edit_task

app_name = 'tasks'
urlpatterns = [
    path('task_creation/', create_task, name='task_creation'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
]
