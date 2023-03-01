from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.PositiveIntegerField()
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField()
    faculty = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    cgpa = models.FloatField()
    # image = models.ImageField(upload_to='passport')

    def __str__(self):
        return f" {self.firstname} {self.lastname}"
    

    