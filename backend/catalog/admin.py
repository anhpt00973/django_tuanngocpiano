from django.contrib import admin
from .models import Brand, Category, Piano, PianoImage


class PianoImageInline(admin.TabularInline):
    model = PianoImage
    extra = 1


@admin.register(Piano)
class PianoAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "price", "condition", "is_published")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PianoImageInline]


admin.site.register(Brand)
admin.site.register(Category)
