from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=30, unique=True)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    department = models.CharField(max_length=100)
    annual_ctc = models.DecimalField(max_digits=12, decimal_places=2)
    experience = models.DecimalField(max_digits=4, decimal_places=1)





class Details(models.Model):
    details = models.TextField()

    def __str__(self):
        return self.details[:100]


class Calendar(models.Model):
    date = models.DateField()
    occasion = models.TextField()

    def __str__(self):
        return str(self.date)    

class JobOpening(models.Model):
    role = models.CharField(max_length=100)
    exp = models.CharField(max_length=50)
    skills = models.CharField(max_length=200)
    ctc = models.CharField(max_length=50)
    notice = models.CharField(max_length=50)