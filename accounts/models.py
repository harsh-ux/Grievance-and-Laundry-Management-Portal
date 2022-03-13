from laundry.models import CHOICES
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Gender(models.Model):
    
    blank_choice = [('', 'Choose')]
    gender_choice = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    gender = models.CharField(max_length=10, choices=blank_choice + gender_choice)

    def __str__(self) -> str:
        return self.gender


class Hostel(models.Model):
    blank_choice = [('', 'Choose')]
    hostel_choice = [
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
        ('B5', 'B5'),
        ('G1', 'G1'),
        ('G2', 'G2'),
        ('G3', 'G3'),
        ('G4', 'G4'),
        ('G5', 'G5'),
        ('G6', 'G6'),
        ('I2', 'I2'),
    ]

    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=blank_choice+hostel_choice)

    def __str__(self) -> str:
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    laundry_id = models.AutoField(primary_key=True, help_text='Unique laundry num. for student table')
    college_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200)
    mobile_num = PhoneNumberField(null=False, blank=True, unique=False)
    room_num = models.CharField(max_length=10)

    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    class Meta:
        # ordering = ['hostel']
        verbose_name_plural = 'Students'


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.AutoField(primary_key=True, help_text='Unique laundry num. for employee table')
    name = models.CharField(max_length=200)
    mobile_num = PhoneNumberField(null=False, blank=True, unique=False)
    
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True)
    

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    class Meta:
        verbose_name_plural = 'Employees'
