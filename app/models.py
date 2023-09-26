from django.db import models

# Create your models here.
class HomePage(models.Model):
    title1 = models.CharField(max_length=55)
    title2 = models.CharField(max_length=55)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title1

class AboutCompany(models.Model):
    img = models.ImageField(upload_to='images/about_company/')
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title 
    

class OurService(models.Model):
    img = models.ImageField(upload_to='images/our_services/')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title 
    
class Client(models.Model):
    img = models.ImageField(upload_to='images/client/')
    username = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Contact(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.message}"
    
class Team(models.Model):
    img = models.ImageField(upload_to='images/team/')
    username = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.username} - {self.profession}"
    
    
