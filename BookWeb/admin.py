from django.contrib import admin
from .models import Book, Review, User


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "rating"]
    list_filter = ("author",)
    search_fields = ("title", "author")


admin.site.register(Review)
admin.site.register(User)
