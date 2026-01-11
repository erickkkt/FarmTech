from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    """Serializer for Animal model"""
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    animal_type_display = serializers.CharField(source='get_animal_type_display', read_only=True)
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)
    
    class Meta:
        model = Animal
        fields = ('id', 'farm', 'farm_name', 'owner', 'owner_username', 'name', 
                  'animal_type', 'animal_type_display', 'breed', 'gender', 'gender_display',
                  'date_of_birth', 'tag_number', 'weight', 'health_status', 'notes',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
