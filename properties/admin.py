from django.contrib import admin
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """
    An admin class for the property model
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
