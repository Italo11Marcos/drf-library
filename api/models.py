from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.ManyToManyField(Author, related_name='authors')
    isbn = models.CharField(max_length=13, null=False, blank=False)
    language = models.CharField(max_length=5, null=False, blank=False)
    num_pages = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title
    
## login: admin
## password: admin123