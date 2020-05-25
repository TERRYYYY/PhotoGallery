from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

class Location(models.Model):
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']
