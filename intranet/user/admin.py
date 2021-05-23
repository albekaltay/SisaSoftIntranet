from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

# Register your models here.


@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username','email')
    fieldsets = UserAdmin.fieldsets + (

        ('Pozisyon', {'fields': ['position']}),

        ('Telefon Numarası ', {'fields': ['telephone_number']}),

        ('Doğum Tarihi', {'fields': ['birthday']}),

        ('Avatar Değiştirme Alan', {'fields': ['avatar']}),


    )


# admin.site.register(CustomUserModel,CustomAdmin)