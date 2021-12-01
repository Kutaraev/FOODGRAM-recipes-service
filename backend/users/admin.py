from django.contrib import admin

from users.models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('email', 'username')
    search_fields = ['email', 'username']
    empty_value_display = "-пусто-"


admin.site.register(User, CustomUserAdmin)
