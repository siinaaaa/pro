from django.contrib import admin

from home.models import Post


# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['name']
