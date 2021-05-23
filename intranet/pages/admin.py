from django.contrib import admin
from .models import Checklist,Checklist2,Checklist3,UserDocuments,UserDocuments2,UserDocuments3

from django.contrib.auth.models import User

# Register your models here.
@admin.register(Checklist)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id','doc_numb','islem') #,'kontrol','description'
    list_display_links = ('id','doc_numb','islem')
    search_fields = ('islem','doc_numb') #,'kontrol'

@admin.register(Checklist2)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id','doc_numb','islem') #,'kontrol','description'
    list_display_links = ('id','doc_numb','islem')
    search_fields = ('islem','doc_numb') #,'kontrol'


@admin.register(Checklist3)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_numb', 'islem')  # ,'kontrol','description'
    list_display_links = ('id', 'doc_numb', 'islem')
    search_fields = ('islem', 'doc_numb')  # ,'kontrol'




@admin.register(UserDocuments)
class UserDocAdmin(admin.ModelAdmin):
    list_display = ('userId','documentNumber','kontrol')
    list_display_links = ('userId','documentNumber')
    search_fields = ('documentNumber__islem','kontrol','userId__username')


@admin.register(UserDocuments2)
class UserDocAdmin(admin.ModelAdmin):
    list_display = ('userId','documentNumber','kontrol')
    list_display_links = ('userId','documentNumber')
    search_fields = ('documentNumber__islem','kontrol','userId__username')


@admin.register(UserDocuments3)
class UserDocAdmin(admin.ModelAdmin):
    list_display = ('userId','documentNumber','kontrol')
    list_display_links = ('userId','documentNumber')
    search_fields = ('documentNumber__islem','kontrol','userId__username')




