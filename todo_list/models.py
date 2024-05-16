from django.db import models

class Todo(models.Model):
    todos = models.CharField(max_length=200)
    dates = models.DateField()


    def __str__(self):
        return self.todos 
