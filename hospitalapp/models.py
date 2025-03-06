from django.db import models

# Create your models here.
class Patient1(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    message = models.TextField()


    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Staff1(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Position = models.CharField(max_length=20)
    Phone = models.CharField(max_length=150)
    email = models.EmailField()
    hire_date = models.DateField()

    def __str__(self):
        return self.Firstname + ""+ self.Lastname

class Ward(models.Model):
    Name = models.CharField(max_length=50)
    Totalbeds = models.IntegerField()
    Availablebeds = models.IntegerField()


    def __str__(self):
        return self.Name



class Appointment2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name