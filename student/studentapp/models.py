from django.db import models
from django.contrib.auth.models import User



class Personal(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='puser')
    Enquiry_no = models.IntegerField(auto_created=True)
    Enquiry_date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=200,blank=True)
    Gender = models.CharField(max_length=50,blank=True)
    Qualification = models.CharField(max_length=100,blank=True)
    Address = models.CharField(max_length=200,blank=True)
    Contact_no = models.IntegerField()
    WhatsApp_no = models.IntegerField()
    DOB = models.DateField(blank=True)


class College(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='coluser')
    College = models.CharField(max_length=200,blank=True)


class Courses(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cuser')
    courses = models.CharField(max_length=200,blank=True)


class Work_experience(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='wuser')
    Experience = models.CharField(max_length=500,blank=True)
