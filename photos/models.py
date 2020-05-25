from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
