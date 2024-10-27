from django.db import models


# Modelul Author
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    # OneToOne: Fiecare autor are o singură editură primară
    primary_publisher = models.OneToOneField(
        "Publisher", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name


# Modelul Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()

    def __str__(self):
        return self.name


# Modelul Series
class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# Modelul Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()

    # ManyToMany: O carte poate avea mai mulți autori, iar un autor poate scrie mai multe cărți
    authors = models.ManyToManyField(Author, related_name="books")

    # ForeignKey (ManyToOne): O carte aparține unei serii, o serie poate avea mai multe cărți
    series = models.ForeignKey(
        Series, on_delete=models.SET_NULL, null=True, blank=True, related_name="books"
    )

    # ManyToOne: O carte poate avea un singur publisher, dar un publisher poate publica mai multe cărți
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="published_books"
    )

    def __str__(self):
        return self.title
