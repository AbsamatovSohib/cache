from rest_framework import generics, status
from product.models import Product
from product.serializer import ProductSerializer
from django.core.cache import cache
from rest_framework.response import Response


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        books = cache.get('book')

        if books is None:
            books = list(Product.objects.all())
            cache.set('book', books, timeout=300)

        else:
            pass

        men = cache.get('book')
        print(men)
        return books



