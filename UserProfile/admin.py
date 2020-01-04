from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
#    form = CustomUserChangeForm
    model = User
    list_display = ('email','is_consultant','is_spoc')
    list_filter = ('email', 'is_consultant','is_spoc',)
    fieldsets = (
        (None, {'fields': ('name','email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_consultant','is_spoc','is_first_time')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email','password1', 'password2',
                       'is_consultant','is_spoc','is_staff','is_active','is_first_time')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)