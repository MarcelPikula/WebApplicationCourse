from django.urls import path
from BookWeb.views import user_view, search_view, add_book, export_data, add_review

urlpatterns = [
    path('mainpage/', user_view, name='mainpage'),
    path('search_results/', search_view, name='search_results'),
    path('add_book/', add_book, name='add_book'),
    path('add_review/', add_review, name='add_review'),
    path('export_data/', export_data, name='export_data'),
]