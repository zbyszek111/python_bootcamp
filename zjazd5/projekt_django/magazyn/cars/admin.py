from django.contrib import admin

from cars.models import Cars

class CarsAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'typ_nadwozia', 'rok_prod', 'engine']


admin.site.register(Cars, CarsAdmin)