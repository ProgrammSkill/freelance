from django.contrib import admin
from ..models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = '__all__'
