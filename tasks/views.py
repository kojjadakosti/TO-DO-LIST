from django.shortcuts import render, HttpResponseRedirect, reverse

from tasks.forms import TaskCreationForm


def index(request):
    return render(request, 'tasks/list.html')


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
