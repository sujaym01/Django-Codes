from django.shortcuts import render
from task.models import TaskModel
# Create your views here.
def show_task(request):
    data = TaskModel.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data' : data})
