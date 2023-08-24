from django.contrib import admin

from .models import Banner


class BannerAdminConfig(admin.ModelAdmin):
    pass


admin.site.register(Banner, BannerAdminConfig)
