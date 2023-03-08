from django.urls import path
from . import views

urlpatterns = [
    path("books/<str:book_id>/copies", views.CopyCreateView.as_view()),
    path("copies/", views.CopyView.as_view()),
    path("copies/<pk>/", views.CopyDetailView.as_view())
]