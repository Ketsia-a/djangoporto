from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.



class ImageTestClass(TestCase):
   # Set up method
    def setUp(self):
        self.picture= Image(name = 'one', description ='art',image = 'vangogh.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.picture,Image))

    def test_save_method(self):
        self.picture.save_image()
        images = Image.objects.all() 
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.picture.save_image()
        self.picture= Image(name = 'one', description ='art',image = 'vangogh.jpg')
        self.picture.save_image()
        self.picture.delete_image()
        deleted = Image.objects.all()
        self.assertEqual(len(deleted),1)

class LocationTestClass(TestCase):

    def setUp(self):
        self.locate= Location(name = 'rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.locate,Location))
       
    def test_save_method(self):
        self.locate.save_location()
        locations = Location.objects.all() 
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.locate.save_location()
        self.locate= Location(name = 'Nairobi')
        self.locate.save_location()
        self.locate.delete_location()
        locat = Location.objects.all()
        self.assertEqual(len(locat),1)    

class CategoryTestClass(TestCase):
    def setUp(self):
        self.categorys= Category(name = 'Art')
 
    def test_instance(self):
        self.assertTrue(isinstance(self.categorys,Category))

    def test_save_method(self):
        self.categorys.save_category()
        category = Category.objects.all() 
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.categorys.save_category()
        self.categorys= Category(name = 'Art')
        self.categorys.save_category()
        self.categorys.delete_category()
        categor = Category.objects.all()
        self.assertEqual(len(categor),1)   


  
