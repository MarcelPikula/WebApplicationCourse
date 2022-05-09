from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
import csv


def export_data(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Description', 'Rating'])

    for book in Book.objects.all().values_list('title', 'author', 'description', 'rating'):
        writer.writerow(book)

    response['Content-Disposition'] = 'attachment; filename = "pomiary.csv"'

    return response


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
    num_of_elements = request.GET.get('number') if request.GET.get('number') else 4
    if request.method == "POST":
        if int(request.POST['ele']) >= 0:
            num_of_elements = request.POST['ele']
        else:
            num_of_elements = 1

    books_paginator = Paginator(all_books, num_of_elements)

    page_num = request.GET.get('page')

    page = books_paginator.get_page(page_num)

    context = {
        'Books': all_books,
        'page': page,
        'elements': num_of_elements,
     }

    return render(request, 'mainpage.html', context)
