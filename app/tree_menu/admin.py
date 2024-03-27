from django.contrib import admin
from .models import MenuItem, Menu

admin.site.register(MenuItem)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
