from django.contrib import admin
from .models import Author, Book, Publisher, Series

# Înregistrează modelele în admin pentru a putea fi gestionate din interfața de administrare
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Series)
