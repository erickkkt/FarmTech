from django.contrib import admin
from .models import Vaccination

@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('vaccine_name', 'animal', 'date_administered', 'next_due_date', 'veterinarian')
    list_filter = ('date_administered', 'next_due_date')
    search_fields = ('vaccine_name', 'animal__tag_number', 'veterinarian')
    readonly_fields = ('created_at', 'updated_at')

