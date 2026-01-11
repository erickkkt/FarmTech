from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model extending Django's AbstractUser"""
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

