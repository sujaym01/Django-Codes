from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, './first_app/home.html',{'data':student})

# def delete_student(request,roll):
#     # std = models.Student.objects.get(pk = roll)
#     # student = models.Student.objects.all()
#     # print(std)
#     # return render(request, './first_app/home.html',{'data':student})

#     std = models.Student.objects.get(pk = roll).delete()
#     print(std)
#     student = models.Student.objects.all()
#     return render(request, './first_app/home.html',{'data':student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk = roll).delete()
    print(std)
    return redirect('homepage')