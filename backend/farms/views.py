from rest_framework import viewsets, permissions
from .models import Farm
from .serializers import FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    """ViewSet for Farm CRUD operations"""
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Farm.objects.all()
        return Farm.objects.filter(owner=user)

