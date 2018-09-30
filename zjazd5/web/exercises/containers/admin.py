from django.contrib import admin
from containers.models import Container

# Register your models here.

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    pass