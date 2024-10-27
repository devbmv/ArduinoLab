from django import forms
from .models import Author, Book, Publisher, Series


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name",
            "birthdate",
            "primary_publisher",
        ]  # câmpurile pe care vrem să le afișăm în formular


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "authors", "series", "publisher"]


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "founded"]


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ["title", "description"]
