# your_app/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, LoginSerializer

# The LoginAPI handles authentication
class LoginAPI(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({
                "status": False,
                "data": serializer.errors
            }, status=400) 
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user_obj = authenticate(username=username, password=password)
        
        if user_obj:
            token, _ = Token.objects.get_or_create(user=user_obj)
            return Response({
                "status": True,
                "data": {'token': str(token)}
            })
        
        return Response({
            "status": False,
            "data": {},
            "message": "Invalid credentials"
        }, status=401) 

#Create an author
class AuthorCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#Create a book
class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#List all books
class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#List all books by a given author
class BooksbyAuthorView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.kwargs.get('author_id')
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset


#Delete book
class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Delete author
class AuthorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

