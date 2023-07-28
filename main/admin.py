from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ("name", "price", "category", "get_photo")
    readonly_fields = ("get_photo",)
    list_display_links = ("name", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name", "category__name")
    list_per_page = 25
    prepopulated_fields = {"slug": ("name", )}

    def get_photo(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='300' />")
    
    get_photo.short_description = "Фотография"

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("get_photo", )
    readonly_fields = ("get_photo",)
    list_per_page = 25

    def get_photo(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='450' />")
    
    get_photo.short_description = "Фотография"

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name", )}


admin.site.site_title = "ИП Петросян"
admin.site.site_header = "ИП Петросян"