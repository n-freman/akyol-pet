from django.db import models
from django.utils.translation import gettext_lazy as _
from translations.models import Translatable


class Banner(Translatable):
    image = models.ImageField(
        _('Image'),
        upload_to='banners'
    )
    active = models.BooleanField(
        _('Is Banner Active'),
        default=True
    )
    title = models.TextField(
        _('Title'),
    )
    subtitle = models.TextField(
        _('Subtitle')
    )

    class TranslatableMeta:
        fields = [
            'title',
            'subtitle'
        ]


class AboutPage(Translatable):
    content = models.TextField(
        _('content')
    )
    image = models.ImageField(
        _('image'),
        upload_to='about-us'
    )

    class Meta:
        verbose_name_plural = 'About Page'

    class TranslatableMeta:
        fields = [
            'content'
        ]

    def __str__(self):
        return 'Change'
