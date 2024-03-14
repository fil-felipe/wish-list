from django.contrib import admin
from .models import GiftUser, GiftList, Gift


@admin.register(GiftUser)
class GiftUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


@admin.register(GiftList)
class GiftListAdmin(admin.ModelAdmin):
    list_display = ['list_name', 'list_user']
    prepopulated_fields = {'slug': ('list_name', )}


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['title', 'gift_list', 'get_user_name'] #'gift_list__list_user'
    prepopulated_fields = {'slug': ('title',)}

