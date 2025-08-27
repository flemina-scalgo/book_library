from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
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
        
        if username == "abcdef" and password == "abc123def":
            user_obj,_ =User.objects.get_or_create(username="abcdef")
            user_obj.set_password("abc123def")
            user_obj.save()


        # user_obj = authenticate(username=username, password=password)
        
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

#Create an author -post
class AuthorCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#Create a book - post
class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#List all books - get
class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#List all books by a given author - get
class BooksbyAuthorView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.kwargs.get('author_id')
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset


#Delete book - delete
class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#Delete author - delete
class AuthorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

