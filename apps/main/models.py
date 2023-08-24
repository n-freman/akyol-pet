from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    image = models.ImageField(
        _('Image'),
        upload_to='banners'
    )
    active = models.BooleanField(
        _('Is Banner Active'),
        default=True
    )
