from django.db import models

# Create your models here.

class Gadget(models.Model):
    productname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    features = models.JSONField(default=list)
    image= models.ImageField(upload_to='gadgets/')

    def __str__(self):
        return self.productname

class ContactDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()    
    
    def __str__(self):
        return self.name
    
# upadate profile
    
# models.py
# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.TextField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
    
#     def __str__(self):
#         return self.user.username
