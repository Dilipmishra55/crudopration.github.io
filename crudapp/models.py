from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.CharField(max_length=10,primary_key=True)
    empname=models.CharField(max_length=50)
    empaddress=models.TextField()
    department=models.CharField(max_length=50)
    salary=models.BigIntegerField()
    