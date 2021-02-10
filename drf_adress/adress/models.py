from django.db import models


class Adress(models.Model):
    cep = models.CharField(max_length=9, null=False)
    complement = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=4, null=False)
    street = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"Adress {self.cep}, {self.complement}, {self.number}"
