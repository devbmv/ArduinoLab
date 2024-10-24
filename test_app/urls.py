from django.urls import path
from .views import (
    main_page,add_all_on_one_page,
    authors_list, books_list, publishers_list, series_list
)

urlpatterns = [
    path('', main_page, name='main_page'),  # Ruta pentru pagina principală

    path('', main_page, name='main_page'),  # Pagina principală
    path('add-all/', add_all_on_one_page, name='add_all'),  # Pagina pentru adăugarea tuturor entităților

    # URL-uri pentru listarea entităților
    path('authors/', authors_list, name='authors_list'),
    path('books/', books_list, name='books_list'),
    path('publishers/', publishers_list, name='publishers_list'),
    path('series/', series_list, name='series_list'),
]
