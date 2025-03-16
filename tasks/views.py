from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404

from tasks.forms import TaskCreationForm
from tasks.models import Task


@login_required(login_url='/users/login/')
def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/list.html', context)

@login_required(login_url='/users/login/')
def create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskCreationForm()
    context = {'form': form}
    return render(request, 'tasks/create.html', context)

@login_required(login_url='/users/login/')
def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskCreationForm(instance=task)
    context = {'form': form, 'task': task}
    return render(request, 'tasks/update.html', context)

def delete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required(login_url='/users/login/')
def details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'tasks/details.html', context)
