from django.contrib import admin
from django.http.request import HttpRequest

from translations.admin import TranslatableAdmin, TranslationInline

from .models import Banner, AboutPage


class BannerAdminConfig(TranslatableAdmin):
    inlines = [TranslationInline, ]


class AboutPageConfig(TranslatableAdmin):
    inlines = [TranslationInline, ]

    def has_add_permission(self, request: HttpRequest) -> bool:
        if AboutPage.objects.count() == 0:
            return True
        return False

    def has_delete_permission(self, request: HttpRequest, obj = None) -> bool:
        return False


admin.site.register(Banner, BannerAdminConfig)
admin.site.register(AboutPage, AboutPageConfig)
