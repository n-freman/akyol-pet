from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline

from .models import BottleCap, Preform


class PreformAdminCofnig(admin.ModelAdmin):
    pass


class BottleCapAdminConfig(TranslatableAdmin):
    inlines = [TranslationInline, ]


admin.site.register(Preform, PreformAdminCofnig)
admin.site.register(BottleCap, BottleCapAdminConfig)
