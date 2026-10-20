from django.contrib import admin

from .models import Hero, Attribute, Position

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Attribute)
admin.site.register(Position)