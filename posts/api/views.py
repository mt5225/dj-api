from ..models import Post, Author
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    print("create posts list view for API")
    serializer_class = serializers.PostSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
