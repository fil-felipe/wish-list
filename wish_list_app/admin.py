from django.contrib import admin
from .models import WishList, Gift


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ["list_name", "list_user"]

    prepopulated_fields = {"slug": ("list_name",)}


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ["title", "gift_list", "get_user_name"]
    prepopulated_fields = {"slug": ("title",)}
