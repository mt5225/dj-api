from ..models import Post, Author
from . import serializers
from rest_framework import generics


class PostListView(generics.ListCreateAPIView):
    """ fetch all posts """
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Post modify"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class AuthorListView(generics.ListCreateAPIView):
    """ return all authors """
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Author modify """
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
