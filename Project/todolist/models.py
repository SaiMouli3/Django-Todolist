from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)  # Allow null values
    completed = models.BooleanField(default=False,blank=True)


    def __str__(self):
        return self.title


