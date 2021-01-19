from django.contrib import admin

# Register your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import UserNet

class UserNetAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Info'), {'fields': ('phone', 'avatar', 'gender', 'birthday', 'technology', 'group')}),
    )
    search_field = ('username')


admin.site.register(UserNet, UserNetAdmin)

