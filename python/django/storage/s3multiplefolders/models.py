from django.db import models
from .custom_storage import S3Folder1Storage, S3Folder2Storage

# Create your models here.

class S3MultipleFolders(models.Model):
    folder1 = models.FileField(storage=S3Folder1Storage)
    folder2 = models.FileField(storage=S3Folder2Storage)