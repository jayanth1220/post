from django.contrib import admin
from .models import Category,Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','Category','created_at']#filds in post 





admin.site.register(Category)
admin.site.register(Post,PostAdmin)
