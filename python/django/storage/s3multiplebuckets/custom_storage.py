from storages.backends.s3boto3 import S3Boto3Storage

class S3DjangoBucket1(S3Boto3Storage):
  location = 'folder'

class S3DjangoBucket2(S3Boto3Storage):
  bucket_name = 'djangobucket2'
  location = 'folder'