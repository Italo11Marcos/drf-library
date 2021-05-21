from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        author = self.get_object()
        serializer = BookSerializer(Book.objects.filter(author=author), many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer