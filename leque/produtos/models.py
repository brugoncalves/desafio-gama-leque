from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


product_status = [
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive")
]


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default="ACTIVE", choices=product_status)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "seller": self.seller,
            "quantity": self.quantity,
            "status": self.status
        }
