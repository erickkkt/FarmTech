from django.db import models
from django.conf import settings

class Vaccination(models.Model):
    """Model representing a vaccination record"""
    animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, related_name='vaccinations')
    vaccine_name = models.CharField(max_length=200)
    date_administered = models.DateField()
    next_due_date = models.DateField(blank=True, null=True)
    veterinarian = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    administered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='vaccinations_administered')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.vaccine_name} - {self.animal.tag_number} - {self.date_administered}"
    
    class Meta:
        db_table = 'vaccinations'
        ordering = ['-date_administered']

