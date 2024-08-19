from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_dispay = ["__all__"]
    list_filter = ["created"]