from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
# Create your views here.



#Create an author
class AuthorCreateView(generics.CreateAPIView):
    queryset =Author.objects.all()
    serializer_class = AuthorSerializer



#Create books with link to author
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#Fetch all books by a given author
class BooksbyAuthorView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.kwargs.get('author_id')
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset

#Delete Book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Delete Author
class AuthorDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer