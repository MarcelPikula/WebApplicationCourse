from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    author = models.CharField(max_length=32, blank=False)
    description = models.TextField(default="", blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=5.00, blank=False)

    def __str__(self):
        return "\"{}\" by {}".format(self.title, self.author)


class User(models.Model):
    username = models.CharField(max_length=16, blank=False, unique=True)
    email = models.EmailField(blank=False)

    def __str__(self):
        return "{}".format(self.username)


class Review(models.Model):
    text_review = models.TextField(default="", blank=False)
    score = models.PositiveSmallIntegerField(default=3)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Review of: {}".format(self.book)



