# Start Project

django-admin startproject storage .

# Install Dependency

pip3 install django-environ django-storages boto3

# Create App

python3 manage.py startapp localands3
python3 manage.py startapp s3multiplefolders
python3 manage.py startapp s3multiplebuckets

# Scenarios

1. Local and S3
   ```python
   from localands3.models import LocalAndS3
   from django.core.files.base import ContentFile
   obj = LocalAndS3()
   obj.local_media.save('localfile.txt', ContentFile(b'content'), save=True)
   obj.s3_media.save('s3file.txt', ContentFile(b's3content'), save=True)
   ```
2. S3 multiple Folders
   ```python
   from s3multiplefolders.models import S3MultipleFolders
   from django.core.files.base import ContentFile
   obj = S3MultipleFolders()
   obj.folder1.save('file1.txt', ContentFile(b'content'), save=True)
   obj.folder2.save('file2.txt', ContentFile(b'content'), save=True)
   ```
3. S3 multiple Buckets
   ```python
   from s3multiplebuckets.models import S3MultipleBuckets
   from django.core.files.base import ContentFile
   obj = S3MultipleBuckets()
   obj.bucket1.save('bucket1.txt', ContentFile(b'content'), save=True)
   obj.bucket2.save('bucket2.txt', ContentFile(b'content'), save=True)
   ```
