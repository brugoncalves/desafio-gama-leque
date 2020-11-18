from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL())
    quantity = models.IntegerField()
    status = {'ATIVO', 'INATIVO'}
