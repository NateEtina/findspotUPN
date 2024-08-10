from django.contrib import admin
from .models import AddressType, Building, Bureau, Local, Office, Space


# A native class to modify the admin display of spot class

@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ('label',)
    list_per_page = 10
    search_fields = ['label']

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    fields = ['name', 'adtype', 'latitude', 'longitude', 'description','burnum', 'localnum', 'interest']
    list_display = ('name', 'adtype','burnum', 'localnum')
    list_filter = ('adtype',)
    list_per_page = 20
    search_fields = ['name']

@admin.register(Bureau)
class BureauAdmin(admin.ModelAdmin):
    fields = ['name', 'adtype', 'latitude', 'longitude', 'description', 'hallnum', 'burbuilding', 'interest']
    list_display = ('name', 'adtype', 'burbuilding', 'hallnum')
    list_filter = ('adtype',)
    list_per_page = 20
    search_fields = ['name']

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    fields = ['name', 'adtype', 'latitude', 'longitude', 'description', 'officebur', 'interest']
    list_display = ('name', 'adtype', 'officebur')
    list_filter = ('adtype',)
    list_per_page = 20
    search_fields = ['name']

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    fields = ['name', 'adtype', 'latitude', 'longitude', 'description', 'burbuilding', 'interest']
    list_display = ('name', 'adtype', 'burbuilding')
    list_filter = ('adtype',)
    list_per_page = 20
    search_fields = ['name']

@admin.register(Space)
class SpotAdmin(admin.ModelAdmin):
    fields = ['name', 'adtype', 'latitude', 'longitude', 'description', 'interest']
    list_display = ('name', 'adtype')
    list_filter = ('adtype',)
    list_per_page = 20
    search_fields = ['name']

"""
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['event_name', 'address', 'event_date', 'event_desc']
    list_display = ('event_name', 'place', 'event_date')
    list_filter = ('event_date','place')
    list_per_page = 10  
    
    """


