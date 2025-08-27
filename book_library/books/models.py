from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    language=models.CharField(max_length=503)

    def __str__(self):
        return f'{self.name}'
    

class Book(models.Model):
    title_of_book = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_of_book}'