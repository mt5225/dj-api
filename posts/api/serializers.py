from ..models import Post, Author
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_featured')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'age', 'sex')
