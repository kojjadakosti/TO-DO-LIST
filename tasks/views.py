from django.shortcuts import render, HttpResponseRedirect, reverse

from tasks.forms import TaskCreationForm
from tasks.models import Task


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/list.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskCreationForm()
    context = {'form': form}
    return render(request, 'tasks/create.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'tasks/update.html', context)