from django.db import models
from .custom_storage import S3MediaStorage
# Create your models here.

class LocalAndS3(models.Model):
  local_media = models.FileField(upload_to='localmedia')
  s3_media = models.FileField(storage=S3MediaStorage)