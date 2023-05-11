# from django.contrib import admin
# from django.contrib.auth.models import Group, User
# from .models import Profile


# # Unregister Groups
# admin.site.unregister(Group)


# # Register your models here.

# # Mix Profile info into User info
# class ProfileInline(admin.StackedInline):
#     model = Profile

# # Extend User model
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     # Display only username fields on admin page
#     fields = ["username"]
#     inlines = [ProfileInline]


# # Unregister initial User 
# admin.site.unregister(User)

# # Reregister User and Profile
# admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Profile


# Unregister Groups
# admin.site.unregister(Group)

admin.site.unregister(User)

# Define Profile as an inline model
class ProfileInline(admin.TabularInline):
    model = Profile

# Extend the UserAdmin class and add the ProfileInline
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [ProfileInline]

# Replace the UserAdmin model with CustomUserAdmin

admin.site.register(User, CustomUserAdmin)

# Register the Profile model separately
admin.site.register(Profile)

