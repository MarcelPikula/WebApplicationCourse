from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Book, Review, User
from .forms import BookForm, ReviewForm
import csv


def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('mainpage')
    return render(request, 'edit_book.html', {'book': book, 'form': form})


def edit_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('mainpage')
    return render(request, 'edit_review.html', {'review': review, 'form': form})


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


def add_review(request):
    submitted = False
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_review.html', {'form': form, 'submitted': submitted})


def search_view(request):
    all_reviews = Review.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'search_results.html', {'searched': searched, 'books': books, 'Reviews': all_reviews})
    else:
        return render(request, 'search_results.html')


def user_view(request):
    user_db = get_user_model()
    all_books = Book.objects.all()
    all_reviews = Review.objects.all()
    all_users = user_db.objects.all()
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
        'Reviews': all_reviews,
        'Users': all_users,
        'page': page,
        'elements': num_of_elements,
     }

    return render(request, 'mainpage.html', context)


def show_users(request):
    user_db = get_user_model()
    all_users = user_db.objects.all()
    return render(request, 'show_users.html', {'Users': all_users})


def show_stats(request):
    user_db = get_user_model()
    all_books = Book.objects.all()
    all_users = user_db.objects.all()
    all_reviews = Review.objects.all()

    context = {
        'num_of_books': len(all_books),
        'num_of_users': len(all_users),
        'num_of_reviews': len(all_reviews),
    }

    return render(request, 'show_stats.html', context)
