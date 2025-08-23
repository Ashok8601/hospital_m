from django.db import models

class User(models.Model):
    name=models.CharField(max_length=18)
    father_name=models. CharField(max_length=30)
    mother=models. CharField(max_length=30)
    Email=models.EmailField(max_length=100)
    mo_no=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    village=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    admit_date=models.DateField()
    deseas=models.CharField(max_length=200)
    medicine=models.CharField(max_length=300)
    notes=models.CharField(max_length=300)
    bed_no=models.IntegerField()
    gardian=models.CharField(max_length=50)
    def __str__(self):
        return self.deseas