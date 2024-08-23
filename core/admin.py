from django.contrib import admin

from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ("nombre","contactado","email","create_at")
    list_filter=("contactado",)