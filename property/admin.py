from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields=["owner"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['likes',]
    inlines = [
        OwnersInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["user", "flat"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "pure_phone"]
    raw_id_fields = ['flats']