from distutils.command.upload import upload
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    roll_num = models.IntegerField()
    image = models.ImageField(upload_to = 'images/')
    


    def __str__(self):
        return self.name
