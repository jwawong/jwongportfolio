from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=64)
  image = models.ImageField(upload_to='static/images/')