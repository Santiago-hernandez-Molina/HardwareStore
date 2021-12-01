from django.db import models
from django.db.models.deletion import CASCADE
from perfiles.models import Perfil 


class Category(models.Model):
    name=models.CharField(max_length=50)
    path=models.FileField(upload_to="")
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    path = models.FileField(upload_to="")
    price = models.FloatField()
    discount = models.FloatField()
    id_seller = models.ForeignKey(Perfil, on_delete=CASCADE)
    category=models.ForeignKey(Category,on_delete=CASCADE)

    class Meta:
        db_table = "products"




