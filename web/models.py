from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Home(models.Model):
    name = models.CharField(max_length=255,null=False)
    img  = models.ImageField(upload_to='pics')
    position = models.TextField()
    name_1 = models.CharField(max_length=200,null=False)
    img_1  = models.ImageField(upload_to='pics')
    position_1 = models.TextField()
    name_2 = models.CharField(max_length=205,null=False)
    img_2  = models.ImageField(upload_to='pics')
    position_2 = models.TextField()
    def __str__(self):
        return self.name




#Registration form
class Login(models.Model):
    username = models.CharField(max_length=255)
    email  = models.EmailField()
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.username

class Prayer(models.Model):
    name = models.CharField(max_length=255)
    email  = models.EmailField()
    subject = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name


class Ministries(models.Model):
    image = models.ImageField(upload_to='pics')
    title  = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title


class Gallary(models.Model):
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.image


class Events(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=255)
    text = models.TextField()
    def __str__(self):
        return self.title



class About(models.Model):
    image = models.ImageField(upload_to='pics')
    title  = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title


class Home_1(models.Model):
    heading= models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.heading


class Construction_history(models.Model):
    image = models.ImageField(upload_to='pics')
    title  = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title
        

class Ben_test(models.Model):
    image = models.ImageField(upload_to='pics')
    name  = models.CharField(max_length=255)
    bio = models.FileField()
    def __str__(self):
        return self.name
