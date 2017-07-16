from django.contrib import admin
from .models import *


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('texto_1', 'ativo',)
    list_display_links = ('texto_1', 'ativo',)
    ordering = ('id',)
    list_filter = ('ativo',)
