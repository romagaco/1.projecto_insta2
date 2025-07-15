from django.contrib import admin
from profiles.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "birth_date", "profile_picture"] 