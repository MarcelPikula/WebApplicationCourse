from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm


def add_book(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_book.html', {'form': form, 'submitted': submitted})


def search_view(request):
    books = []
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'search_results.html', {'searched': searched, 'books': books})
    else:
        return render(request, 'search_results.html')


def user_view(request):
    all_books = Book.objects.all()

    books_paginator = Paginator(all_books, 4)

    page_num = request.GET.get('page')

    page = books_paginator.get_page(page_num)

    book_handler = []

    context = {
        'Books': all_books,
        'page': page,
        'book_handler': book_handler,
    }

    return render(request, 'mainpage.html', context)
