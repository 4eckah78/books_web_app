from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Book
from .serializers import BookSerializer


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.book1 = Book.objects.create(
            id=1, title="Война и мир", author="Лев Толстой", published_year=1869
        )
        self.book2 = Book.objects.create(
            id=2, title="Анна Каренина", author="Лев Толстой", published_year=1877
        )
        self.book3 = Book.objects.create(
            id=3, title="Евгений Онегин", author="Александр Пушкин", published_year=1833
        )
        self.book4 = Book.objects.create(
            id=4,
            title="Преступление и наказание",
            author="Федор Достоевский",
            published_year=1866,
        )

        self.book_url = reverse("books")
        self.book_detail_url = reverse("book", kwargs={"pk": self.book1.pk})

    def test_book_list(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSerializer(
            [self.book1, self.book2, self.book3, self.book4], many=True
        ).data
        self.assertEqual(response.data, expected_data)

    def test_book_list_filtered_author(self):
        url = self.book_url + "?author=Лев Толстой"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSerializer([self.book1, self.book2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_book_list_filtered_author_no_match(self):
        url = self.book_url + "?author=Толстой"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_book_detail(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookSerializer(self.book1).data
        self.assertEqual(response.data, expected_data)

    def test_create_book(self):
        new_book_data = {
            "id": 5,
            "title": "Новая книга",
            "author": "Новый автор",
            "published_year": 2023,
        }
        response = self.client.post(self.book_url, new_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5)
        self.assertEqual(Book.objects.get(pk=5).title, "Новая книга")
