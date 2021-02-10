from django.db import models
import requests

class Adress(models.Model):
    cep = models.CharField(max_length=7, null=False)
    complement = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=4, null=False)
    street = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"Adress {self.cep}, {self.complement}, {self.number}"
