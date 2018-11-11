from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    headcount = models.PositiveIntegerField()
    
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ID_number = models.CharField(max_length=20)
    its_school = models.ForeignKey(School, on_delete=models.CASCADE)
