from django.urls import path

from tasks.views import create, edit, delete, details

app_name = 'tasks'
urlpatterns = [
    path('create_task/', create, name='create'),
    path('edit_task/<int:task_id>', edit, name='edit'),
    path('delete_task/<int:task_id>', delete, name='delete'),
    path('details/<int:task_id>', details, name='details'),
]
