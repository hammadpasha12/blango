from django.contrib import admin
from blogs.models import Tag, Post

# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):  
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "published_at")
    search_fields = ("title",)
    list_filter = ("published_at",)
    

admin.site.register(Post, PostAdmin)
