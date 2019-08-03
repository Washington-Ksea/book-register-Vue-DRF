from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop1.models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """BookオブジェクトのCRUDを実行するAPI"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
