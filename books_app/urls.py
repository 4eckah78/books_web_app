from django.urls import path

from .views import BookList, PutGetDeleteOneBook

urlpatterns = [
    path("books/", BookList.as_view(), name="books"),
    path("books/<int:pk>/", PutGetDeleteOneBook.as_view(), name="book"),
]
