from django.contrib import admin

from .models import Dadata


class DadataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dadata)
