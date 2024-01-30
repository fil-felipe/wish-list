from django.contrib import admin
from .models import PresentUser, PresentList, Present

admin.site.register(PresentUser)
admin.site.register(PresentList)
admin.site.register(Present)
# Register your models here.
