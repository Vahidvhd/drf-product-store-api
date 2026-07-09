from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend


from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [                           
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

  
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id'] 


class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [ 
        DjangoFilterBackend,                          
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['category', 'is_active']
    search_fields = ['name']
    ordering_fields = ['id', 'name', 'price', 'created_at']
    ordering = ['id']