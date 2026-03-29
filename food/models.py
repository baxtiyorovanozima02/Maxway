from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='foods/')
