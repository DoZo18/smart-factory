from django.contrib import admin

# Register your models here.
from .models import SensorData

admin.site.register(SensorData)