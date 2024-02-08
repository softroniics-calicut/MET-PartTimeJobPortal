from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Login1(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    usertype=models.IntegerField(null=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    login_id = models.ForeignKey(Login1, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    # username = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=30, null=True)
    phone = models.IntegerField(null=True)
    qualification = models.CharField(max_length=30, null=True)
    resume = models.FileField(null=True)
    # password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.login_id.username

class Agency(models.Model):
    login_id=models.ForeignKey(Login1,on_delete=models.CASCADE,null=True)
    # username=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=30,null=True)
    address=models.CharField(max_length=100,null=True)
    # gender=models.CharField(max_length=30,null=True)
    phone=models.IntegerField(null=True)
    image=models.FileField(null=True)
    # password=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.login_id.username



class Job(models.Model):
    agency_id=models.ForeignKey(Agency,on_delete=models.CASCADE,null=True)
    jobname=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=40,null=True)
    salary=models.IntegerField(null=True)
    description=models.CharField(max_length=70,null=True)


    def __str__(self):
        return self.jobname

class Application(models.Model):
    application_choices = (
        ('pending','pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),

    )
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    std_id=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    date=models.DateField(default=timezone.now,null=True)
    status=models.CharField(max_length=50,choices=application_choices, default='pending')
    resume=models.FileField(null=True)
    description=models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.status

