from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=255, blank=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length=255, blank=True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images


    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']

class Image(models.Model):
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    image_file = models.ImageField(upload_to='images/', default='')
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image(request, id):
        locations = Location.get_location()
        try:
          image = Image.objects.get(pk=id)
          print(image)

        except ObjectDoesNotExist:
          raise Http404()

        return image

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

