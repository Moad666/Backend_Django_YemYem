from django.db import models

# Create your models here.


class Recipe(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=400)
    Ingredients = models.CharField(max_length=300)
    image = models.CharField(max_length=1000)


