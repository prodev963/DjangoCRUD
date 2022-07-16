from django.db import models
from enum import Enum
from django.core.validators import RegexValidator
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    class Gender(models.TextChoices):
        male = 'male'
        female = 'female'

    name = models.CharField(max_length=256)
    course = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=Gender.choices)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("my_app:student_detail",kwargs={'pk':self.pk})    
    