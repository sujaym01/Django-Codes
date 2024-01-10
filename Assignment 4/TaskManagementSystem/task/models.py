from django.db import models
from category.models import TaskCategoryModel
# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length= 100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(TaskCategoryModel)

    def __str__(self):
        return self.task_title