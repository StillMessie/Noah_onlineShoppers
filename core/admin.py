from django.contrib import admin

# Register your models here.

from .models import Item, OderItem, Oder

admin.site.register(Item)
admin.site.register(OderItem)
admin.site.register(Oder)
