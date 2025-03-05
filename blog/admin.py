from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created", "updated")
    list_filter = ("status", "created", "updated")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created"
    ordering = ("status", "created")

admin.site.register(Post, PostAdmin)