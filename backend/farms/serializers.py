from rest_framework import serializers
from .models import Farm

class FarmSerializer(serializers.ModelSerializer):
    """Serializer for Farm model"""
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Farm
        fields = ('id', 'owner', 'owner_username', 'name', 'location', 'size', 
                  'description', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
