from django.db import models
from django.conf import settings

class Animal(models.Model):
    """Model representing an animal"""
    ANIMAL_TYPE_CHOICES = (
        ('cattle', 'Cattle'),
        ('goat', 'Goat'),
        ('sheep', 'Sheep'),
        ('pig', 'Pig'),
        ('poultry', 'Poultry'),
        ('other', 'Other'),
    )
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    farm = models.ForeignKey('farms.Farm', on_delete=models.CASCADE, related_name='animals')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='animals')
    name = models.CharField(max_length=100, blank=True, null=True)
    animal_type = models.CharField(max_length=20, choices=ANIMAL_TYPE_CHOICES)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    tag_number = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, help_text="Weight in kg")
    health_status = models.CharField(max_length=100, default='Healthy')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.tag_number} - {self.get_animal_type_display()}"
    
    class Meta:
        db_table = 'animals'
        ordering = ['-created_at']

