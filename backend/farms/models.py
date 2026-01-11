from django.db import models
from django.conf import settings

class Farm(models.Model):
    """Model representing a farm"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    size = models.DecimalField(max_digits=10, decimal_places=2, help_text="Size in hectares")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.owner.username}"
    
    class Meta:
        db_table = 'farms'
        ordering = ['-created_at']

