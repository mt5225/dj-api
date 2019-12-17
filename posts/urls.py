from django.urls import path
from .api import views

urlpatterns = [
    path('posts', views.PostListView.as_view()),
    path('posts/<int:pk>', views.PostDetailView.as_view()),
    path('authors', views.AuthorListView.as_view()),
    path('authors/<int:pk>', views.AuthorDetailView.as_view())
]
