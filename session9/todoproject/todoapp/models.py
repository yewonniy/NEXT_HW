from django.db import models
import datetime 

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField()
    dueday = models.DateField()

    def __str__(self):
        return self.title