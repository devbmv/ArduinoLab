"""custom_storages.py: defines the storage location for static and media files
for production."""

# - - - - - Django Imports - - - - - - - - -
from django.conf import settings

# - - - - - 3rd party Imports - - - - - - - -
from storages.backends.s3boto3 import S3Boto3Storage

# pylint: disable=W0223


class StaticStorage(S3Boto3Storage):
    """Sets the storage location for static files on AWS."""

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Sets the storage location for media files on AWS."""

    location = settings.MEDIAFILES_LOCATION
