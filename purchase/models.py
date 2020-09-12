from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class ShoppingCart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_num = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=True)
    