from django.contrib import admin
from django.http.request import HttpRequest
from translations.admin import TranslatableAdmin, TranslationInline

from .models import AboutPage, Banner, FeedBack


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


class FeedbackAdminConfig(admin.ModelAdmin):
    list_display = ['sender', 'subject', 'message']

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False
    
    def has_add_permission(self, *args, **kwargs) -> bool:
        return False


admin.site.register(AboutPage, AboutPageConfig)
admin.site.register(Banner, BannerAdminConfig)
admin.site.register(FeedBack, FeedbackAdminConfig)
