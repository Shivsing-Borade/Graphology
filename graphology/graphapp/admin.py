from django.contrib import admin

# Register your models here.

from .models import Image

@admin.register(Image)

#admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','image']