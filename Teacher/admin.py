from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as UserAdmin
# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ('email', 'username','date_joined', 'is_admin', 'is_staff','phone_no')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.unregister(Group)
admin.site.register(User,MyUserAdmin)
