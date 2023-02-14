from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_list.models import Task


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date_to_do': request.POST.get('date_to_do'),
    }
    task = Task.objects.create(**task_data)
    return redirect(f'/task/?pk={task.pk}')

def detail_view(request):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {'task': task}
    return render(request, 'task.html', context=context)

def delete_view(request):
    task_pk = request.GET.get('pk')
    Task.objects.get(pk=task_pk).delete()
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context=context)

