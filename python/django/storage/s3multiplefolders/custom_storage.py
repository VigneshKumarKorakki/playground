from storages.backends.s3boto3 import S3Boto3Storage

class S3Folder1Storage(S3Boto3Storage):
  location = 'folder1'

class S3Folder2Storage(S3Boto3Storage):
  location = 'folder2'