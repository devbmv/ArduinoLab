from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static"  # Locația fișierelor statice în bucket-ul S3
    default_acl = 'public-read'  # Asigură acces public la fișierele statice

class MediaStorage(S3Boto3Storage):
    location = "media"  # Locația fișierelor media în bucket-ul S3
    default_acl = 'public-read'  # Asigură acces public la fișierele media
