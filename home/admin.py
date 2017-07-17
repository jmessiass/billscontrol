from django.contrib import admin
from .models import *


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('texto_1', 'ativo',)
    list_display_links = ('texto_1', 'ativo',)
    ordering = ('id',)
    list_filter = ('ativo',)


@admin.register(Duvida)
class DuvidaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email',)
    list_display_links = ('nome', 'email',)
    ordering = ('id',)


@admin.register(ComoFunciona)
class ComoFuncionaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo',)
    list_display_links = ('titulo', 'ativo',)
    ordering = ('id',)
    list_filter = ('ativo',)
