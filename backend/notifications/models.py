from django.db import models
from django.conf import settings

class Notification(models.Model):
    """Model representing a notification"""
    NOTIFICATION_TYPE_CHOICES = (
        ('vaccination', 'Vaccination Due'),
        ('system', 'System'),
        ('marketplace', 'Marketplace'),
        ('general', 'General'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        db_table = 'notifications'
        ordering = ['-created_at']

