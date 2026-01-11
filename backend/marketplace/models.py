from django.db import models
from django.conf import settings

class Product(models.Model):
    """Model representing a marketplace product"""
    CATEGORY_CHOICES = (
        ('animal', 'Animal'),
        ('feed', 'Feed'),
        ('equipment', 'Equipment'),
        ('medicine', 'Medicine'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('pending', 'Pending'),
    )
    
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products_sold')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    location = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.seller.username}"
    
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

