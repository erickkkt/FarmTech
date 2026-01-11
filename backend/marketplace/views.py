from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for Product CRUD operations"""
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    
    def get_queryset(self):
        user = self.request.user
        if self.action in ['list', 'retrieve']:
            return Product.objects.filter(status='available')
        if user.user_type == 'admin':
            return Product.objects.all()
        return Product.objects.filter(seller=user)

