from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.LoginAPI.as_view(), name='api-login'),
    path('authors/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/by-author/<int:author_id>/', views.BooksbyAuthorView.as_view(), name='books-by-author'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]