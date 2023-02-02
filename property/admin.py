from django.contrib import admin
from .models import Flat, Complaint

# admin.site.register(admin.ModelAdmin)
@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['likes']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["user", "flat"]