import django_filters
from django_filters import rest_framework as filters

from .models import Book


class BookFilter(filters.FilterSet):
    author = django_filters.CharFilter(field_name="author", lookup_expr="iexact")

    class Meta:
        model = Book
        fields = ["author"]
