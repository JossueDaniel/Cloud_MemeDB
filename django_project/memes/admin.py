from django.contrib import admin

from .models import Meme, Tag

# Register your models here.
class TagInLine(admin.TabularInline):
    model = Tag
    extra = 1

class MemeAdmin(admin.ModelAdmin):
    inlines = [TagInLine]
    list_display = ['id', 'image', 'user', 'uploaded_at']

admin.site.register(Meme, MemeAdmin)
admin.site.register(Tag)
