from django.contrib import admin
from engines.models import Engine

# Register your models here.

class EngineAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'pojemnosc', 'ilosc_cyl', 'rodzaj_silnika', 'opis']


admin.site.register(Engine, EngineAdmin)