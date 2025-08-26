from django.urls import path
from .views import AuthorCreateView,BookCreateView,BookListView,BooksbyAuthorView,BookDeleteView,AuthorDeleteView


urlpatterns= [
    path("author/create/",AuthorCreateView.as_view(), name="author-create"),
    path("book/create/",BookCreateView.as_view(),name="book-create"),
    path("booklist",BookListView.as_view(),name="book-list"),
    path("author/<int:author_id>/books/",BooksbyAuthorView.as_view(),name="books-by-author"),
    path("book/<int:pk>/delete/",BookDeleteView.as_view(),name="book-delete"),
    path("author/<int:pk>/delete/",AuthorDeleteView.as_view(),name="author-delete"),
]