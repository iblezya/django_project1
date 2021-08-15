from django.db import models

# Create your models here.
class Products(models.Model):
  cod_product = models.IntegerField()
  description = models.CharField(max_length=150)
  create      = models.DateTimeField(auto_now_add=True)
  category    = models.CharField(max_length=150)
  price       = models.FloatField()
  stock       = models.IntegerField()

def __str__(self):
  return self.cod_product
