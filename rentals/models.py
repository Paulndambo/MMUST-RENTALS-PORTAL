from django.db import models
from django.urls import reverse

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('owners')


class Rental(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    unit_rent = models.IntegerField()
    occupied = models.IntegerField()
    vacant = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)

class Student(models.Model):
    name = models.CharField(max_length=255)
    reg_number = models.CharField(max_length=255, unique=True)
    id_number = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=255, choices=(('female', 'Female'),('male', 'Male')))
    room_number = models.CharField(max_length=255)
    county = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    