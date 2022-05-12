from django.urls import path
from BookWeb.views import user_view, search_view, add_book, export_data, add_review, show_users, show_stats, edit_review, edit_book

urlpatterns = [
    path('mainpage/', user_view, name='mainpage'),
    path('search_results/', search_view, name='search_results'),
    path('add_book/', add_book, name='add_book'),
    path('add_review/', add_review, name='add_review'),
    path('show_users/', show_users, name='show_users'),
    path('show_stats/', show_stats, name='show_stats'),
    path('export_data/', export_data, name='export_data'),
    path('edit_book/<book_id>', edit_book, name='edit_book'),
    path('edit_review/<review_id>', edit_review, name='edit_review'),
]