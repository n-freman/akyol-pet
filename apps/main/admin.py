from django.contrib import admin

from translations.admin import TranslatableAdmin, TranslationInline

from .models import Banner


class BannerAdminConfig(TranslatableAdmin):
    inlines = [TranslationInline, ]



admin.site.register(Banner, BannerAdminConfig)
