from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
       return self.name
     
    def save_location(self):
       self.save()   
    
    @classmethod
    def get_locations(cls):
       locations = Location.objects.all()
       return locations
    

    @classmethod
    def update_location(cls, pk, value):
       cls.objects.filter(pk=pk).update(image=value)
    

    def delete_location(self):
       self.delete()


class Category(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
       return self.name
    

    def save_category(self):
       self.save()
    

    def delete_category(self):
       self.delete()

class Image(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete =models.SET_NULL,null =True)
    category = models.ForeignKey(Category,on_delete =models.SET_NULL,null =True)
    pub_date = models.DateTimeField(auto_now_add =True,null=True)
    image = models.ImageField(upload_to = 'pictures/',null=True)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()    

    @classmethod
    def update_image(cls, pk, value):
        cls.objects.filter(pk =pk).update(image=value)

    @classmethod
    def get_image_by_pk(cls, pk):
        cls.objects.filter(pk =pk).all()
        return image 

    @classmethod
    def search_by_category(cls, category):
        image = cls.objects.filter(category__name__icontains=category)    
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = cls.objects.filter(location__name=location).all()
        return image    