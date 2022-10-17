from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from accounts import models

# Register your models here.


class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    readonly_fields = ('date_joined', 'last_activity', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'is_active', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', )}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        })

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'username',
                    'date_joined', 'first_name', 'last_name', 'is_staff',)
    search_fields = ('email', 'username',
                     'date_joined', 'first_name', 'last_name',)
    ordering = ('date_joined',)


class UserProfileAdmin(admin.ModelAdmin):
    model = models.UserProfile

    list_display = (
        'user',
        'country',
        'city',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
    )


admin.site.register(models.UserProfile, UserProfileAdmin)


admin.site.register(models.User, UserAdmin)