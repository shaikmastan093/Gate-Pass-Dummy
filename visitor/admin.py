# admin.py
from django.contrib import admin
from .models import VisitorTable

@admin.register(VisitorTable)
class VisitorTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'gatepass_id', 'in_time', 'out_time', 'approval_status')
    search_fields = ('name', 'mobile', 'gatepass_id')
