from django.contrib import admin
from .models import User, Address
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name','last_name', 'is_staff']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (_('authentication data'), {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('display_name',)
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser',)
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )


class UserAddressesItemInline(admin.TabularInline):
    model = Address
    fields = ("address", "postal_code")
    extra = 1
    show_change_link = True


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserAddressesItemInline]


admin.site.register(User, UserAdmin)
admin.site.register(Address)
# Register your models here.
