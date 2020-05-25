from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.new_location = Location(location = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class CategoryTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.new_category = Category(category = 'Food')
    
    def test_save(self):
        self.new_category.save()

        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class ImageTestClass(TestCase):
    
    def SetUp(self):
        self.image = Image(title = 'BB', description ='Test Description', location = self.new_location, category = self.new_category, image ='/media/images/ilnur-kalimullin-kP1AxmCyEXM-unsplash2.jpg')

        self.image.save_image()

        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

        Image.del_photo(self.image.id)        

        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

