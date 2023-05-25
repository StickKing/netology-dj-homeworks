from django.contrib import admin
from .models import *

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'date_time', 'sensor')
    list_filter = ('temperature', 'date_time', 'sensor')