from ast import mod
from encodings.punycode import T

from django.db import models


class Book(models.Model):
    id: int = models.IntegerField(primary_key=True)
    title: str = models.CharField(max_length=100, blank=False)
    author: str = models.CharField(max_length=100, blank=False)
    published_year: str = models.PositiveSmallIntegerField(blank=False)
