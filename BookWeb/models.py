from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    author = models.CharField(max_length=32, blank=False)
    description = models.TextField(default="", blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=5.00, blank=False)

    def __str__(self):
        return "\"{}\" by {}".format(self.title, self.author)
