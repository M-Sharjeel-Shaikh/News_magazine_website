from django.db import models

# Create your models here.
class Subscriber(models.Model):
    Email=models.CharField(max_length=30)