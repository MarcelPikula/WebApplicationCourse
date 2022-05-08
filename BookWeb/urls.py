from django.urls import path
from BookWeb.views import user_view, search_view, add_book

urlpatterns = [
    path('mainpage/', user_view, name='mainpage'),
    path('search_results/', search_view, name='search_results'),
    path('add_book/', add_book, name='add_book'),
]