from django.contrib import admin
from .models import Author,Book

# Register your models here.


@admin.register(Author)
class Author_Admin(admin.ModelAdmin):
    list_display = ('id','name','language')
    search_fields = ('name','books__title_of_book')


@admin.register(Book)
class Book_Admin(admin.ModelAdmin):
    list_display = ('id','title_of_book','year','author')
    search_fields=('title_of_book','author')
