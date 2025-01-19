from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at', 'updated_at', 'is_staff', 'is_active']
    search_fields = ['email', 'username']

admin.site.register(User, UserAdmin)
