from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline

from .models import BottleCap, Preform


class PreformAdminCofnig(admin.ModelAdmin):
    list_display = ['code', 'thread_standard', 'weight', 'height']


class BottleCapAdminConfig(TranslatableAdmin):
    list_display = ['code', 'raw_materials']
    inlines = [TranslationInline, ]


admin.site.register(Preform, PreformAdminCofnig)
admin.site.register(BottleCap, BottleCapAdminConfig)
