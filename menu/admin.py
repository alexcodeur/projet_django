from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')  # Affiche le champ 'order' dans l'admin
    ordering = ['order']  # Permet de trier les éléments dans l'ordre que tu as défini

admin.site.register(MenuItem, MenuItemAdmin)