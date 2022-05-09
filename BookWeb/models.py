from django.db import models


class LibraryInfo(models.Model):
    STORAGES = {
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    }

    BOOKSTANDS = {
        (0, 'Front'),
        (1, 'Back'),
        (2, 'Left'),
        (3, 'Right'),
    }

    storage = models.PositiveSmallIntegerField(choices=STORAGES, blank=False, default=0)
    bookstand = models.PositiveSmallIntegerField(choices=BOOKSTANDS, blank=False, default=0)

    def __str__(self):
        return "Storage: {}, Bookstand: {}".format(self.storage, self.bookstand)


class Book(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    author = models.CharField(max_length=32, blank=False)
    description = models.TextField(default="", blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=5.00, blank=False)
    library_info = models.OneToOneField(LibraryInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "\"{}\" by {}".format(self.title, self.author)


class Review(models.Model):
    text_review = models.TextField(default="", blank=False)
    score = models.PositiveSmallIntegerField(default=3)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)