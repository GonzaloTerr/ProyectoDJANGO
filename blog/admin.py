from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class postResource(admin.ModelAdmin):
    model = Post
    list_display = ("title","show_home","pk","autor","create_at")
       

