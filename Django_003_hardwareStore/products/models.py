from django.db import models
from django.db.models.deletion import CASCADE


class Seller(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "sellers"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    path = models.FileField(upload_to="")
    price = models.FloatField()
    discount = models.FloatField()
    id_seller = models.ForeignKey(Seller, on_delete=CASCADE)

    class Meta:
        db_table = "products"
