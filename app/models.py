from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    publication_date = models.DateField()
    publisher =models.CharField(max_length=200)
    summary = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    link = models.URLField(max_length=1024)
    cover_image = models.URLField(max_length=1024)

    def __str__(self):
        return self.title

