from rest_framework import viewsets, permissions
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    """ViewSet for Animal CRUD operations"""
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Animal.objects.all()
        return Animal.objects.filter(owner=user)

