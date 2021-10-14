from django.contrib import admin
from django.db.models.fields import TextField
from .models import post

# Register your models here.

class postAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(post, postAdmin)