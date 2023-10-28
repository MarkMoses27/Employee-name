from django.db import models
from django.utils.text import slugify

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False)

 
    def __str__(self):
        return self.name
