from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'envsync/static/'
    default_acl = 'public-read'

    
class PublicMediaStorage(S3Boto3Storage):
    location = 'envsync/media/'
    default_acl = 'public-read'
    file_overwrite = False
  

    