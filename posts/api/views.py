from ..models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
