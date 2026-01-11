from rest_framework import viewsets, permissions
from .models import Vaccination
from .serializers import VaccinationSerializer

class VaccinationViewSet(viewsets.ModelViewSet):
    """ViewSet for Vaccination CRUD operations"""
    serializer_class = VaccinationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Vaccination.objects.all()
        return Vaccination.objects.filter(animal__owner=user)

