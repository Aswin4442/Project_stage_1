from django.db import models

# Create your models here.

# class product(models.Model):
#     username = models.CharField(max_length=100)
#     productname = models.CharField(max_length=100)
#     deliveryaddress = models.CharField(max_length=200)
#     phonenumber = models.IntegerField()
#     productprice = models.IntegerField()

#     def __str__(self):
#         return self.username

class ContactDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()    
    
    def __str__(self):
        return self.name