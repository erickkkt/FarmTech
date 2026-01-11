from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('tag_number', 'name', 'animal_type', 'breed', 'farm', 'owner', 'health_status', 'created_at')
    list_filter = ('animal_type', 'gender', 'health_status', 'created_at')
    search_fields = ('tag_number', 'name', 'breed', 'owner__username', 'farm__name')
    readonly_fields = ('created_at', 'updated_at')

