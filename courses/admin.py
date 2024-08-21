from django.contrib import admin
from .models import Course
# Register your models here.

@admin.register(Course)
class courseResource(admin.ModelAdmin):
    model = Course
    list_display = ("title","show_home","create_at")
