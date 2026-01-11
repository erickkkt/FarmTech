from django.contrib import admin
from .models import Farm

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location', 'size', 'created_at')
    list_filter = ('created_at', 'owner')
    search_fields = ('name', 'location', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

