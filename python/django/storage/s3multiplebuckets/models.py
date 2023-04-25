from django.db import models
from .custom_storage import S3DjangoBucket1, S3DjangoBucket2

# Create your models here.

class S3MultipleBuckets(models.Model):
  bucket1 = models.FileField(storage=S3DjangoBucket1)
  bucket2 = models.FileField(storage=S3DjangoBucket2)
  