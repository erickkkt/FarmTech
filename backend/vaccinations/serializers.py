from rest_framework import serializers
from .models import Vaccination

class VaccinationSerializer(serializers.ModelSerializer):
    """Serializer for Vaccination model"""
    animal_tag = serializers.CharField(source='animal.tag_number', read_only=True)
    administered_by_username = serializers.CharField(source='administered_by.username', read_only=True)
    
    class Meta:
        model = Vaccination
        fields = ('id', 'animal', 'animal_tag', 'vaccine_name', 'date_administered', 
                  'next_due_date', 'veterinarian', 'batch_number', 'notes',
                  'administered_by', 'administered_by_username', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        if 'administered_by' not in validated_data:
            validated_data['administered_by'] = self.context['request'].user
        return super().create(validated_data)
