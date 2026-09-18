from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)