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

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

class CategoryTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.new_category = Category(category = 'Food')
    
    def test_save(self):
        self.new_category.save()

        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']

class ImageTestClass(TestCase):
    
    def SetUp(self):
        self.image = Image(title = 'BB', description ='Test Description', location = self.new_location, category = self.new_category, image ='/media/images/ilnur-kalimullin-kP1AxmCyEXM-unsplash2.jpg')

        self.image.save_image()

        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

        Image.del_photo(self.image.id)        

        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    @classmethod
    def get_image(request, id):
        locations = Location.get_location()
        try:
          image = Image.objects.get(pk=id)
          print(image)

        except ObjectDoesNotExist:
          raise Http404()

        return image

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()   

