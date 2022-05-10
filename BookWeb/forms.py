from django import forms
from django.forms import ModelForm
from .models import Book, Review, User


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
        all_users = User.objects.all()
        model = Review
        fields = "__all__"

        labels = {
            'text_review': '',
            'score': '',
        }

        widgets = {
            'text_review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Review'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        labels = {
            'username': '',
            'email': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}),
        }
