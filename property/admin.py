from django.contrib import admin
from .models import Flat

# admin.site.register(admin.ModelAdmin)
@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']


