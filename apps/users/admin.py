from django.contrib import admin

# Register your models here.
from apps.users import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
    list_display_links = ('id', 'username')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)