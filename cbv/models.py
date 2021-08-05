from django.db import models

# Create your models here.
class Stuadd(models.Model):
    male_female = (('Male','male'),('Female','female'))
    sname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=male_female)
    dob = models.DateField()
    email= models.EmailField()
    phone = models.BigIntegerField()