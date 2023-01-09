from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    subject = models.CharField(max_length=500)
    message=models.TextField(max_length=1500, blank=False)