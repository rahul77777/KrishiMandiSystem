from django.contrib import admin
from .models import Godown, Storage
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class GodownAdmin(LeafletGeoAdmin):
	list_display = ('Name','Location')

class StorageAdmin(LeafletGeoAdmin):
	list_display = ('Name_of_Godown','City')


admin.site.register(Godown,GodownAdmin)
admin.site.register(Storage,StorageAdmin)