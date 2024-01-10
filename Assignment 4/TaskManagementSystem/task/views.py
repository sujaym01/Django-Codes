from django.shortcuts import render,redirect
from .forms import TaskForm
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            # print(task_form.cleaned_data)
            task_form.save()
    else:
        task_form = TaskForm()
    return render(request, 'task/add_task.html', {'form': task_form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task_form = TaskForm(instance=task)
    print(task.task_title)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task) 
        if task_form.is_valid(): 
            task_form.save() 
            return redirect('homepage') 
    
    return render(request, 'task/add_task.html', {'form' : task_form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')
