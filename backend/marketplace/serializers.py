from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""
    seller_username = serializers.CharField(source='seller.username', read_only=True)
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'seller', 'seller_username', 'title', 'description', 
                  'category', 'category_display', 'price', 'quantity', 
                  'status', 'status_display', 'image', 'location',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)
