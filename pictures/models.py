from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
       return self.name

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
       return self.name
