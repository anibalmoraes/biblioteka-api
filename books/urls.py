from django.urls import path
from .views import BookView, BookDetailView, FollowingView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<pk>/", BookDetailView.as_view()),
    path("books/<pk>/follow/", FollowingView.as_view()),
]
