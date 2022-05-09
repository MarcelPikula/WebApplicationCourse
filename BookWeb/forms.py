from django import forms
from django.forms import ModelForm
from .models import Book, Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels = {
            'title': '',
            'author': '',
            'description': '',
            'rating': 'Rating',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {
            'text_review': '',
            'score': '',
            'book': '',
        }

        widgets = {
            'text_review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Review'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
        }
