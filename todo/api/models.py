from django.db import models

# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length=200)
    summary=models.CharField(max_length=300,null=True)
    status =models.BooleanField(default=False,null=True)

    def __str__(self) -> str:
        return self.title
