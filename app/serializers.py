from django.forms import widgets
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', )

class BookSerializer(serializers.ModelSerializer):
    # books can have more than one author so we'll represent the author
    # value with the 'name' field
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'publisher', 'summary', 'price', 'link', 'cover_image', )

