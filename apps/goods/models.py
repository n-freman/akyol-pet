from django.db import models
from django.utils.translation import gettext_lazy as _
from translations.models import Translatable


class Preform(models.Model):
    code = models.IntegerField(_("code"), primary_key=True)
    thread_standard = models.CharField(
        _("Thread standard"),
        max_length=120
    )
    weight = models.IntegerField(_("Weight"), )
    height = models.FloatField(_("Height"), null=True)
    blown_volume = models.FloatField(_("Blown volume"), )
    image = models.ImageField(_("Image"), upload_to='preforms')
    slug = models.SlugField(_("Slug"), )

    class Meta:
        verbose_name = _('Preform')
        verbose_name_plural = _('Preforms')


class BottleCap(Translatable):
    code = models.IntegerField(
        _("code"), 
        primary_key=True
    )
    raw_materials = models.CharField(
        _("Raw materials"), 
        max_length=120
    )
    application = models.CharField(
        _("Application"),
         max_length=255
    )
    logo = models.CharField(
        _("Logo"), 
        max_length=255
    )
    manufacturing_technology = models.CharField(
        _("Manufacturing technology"),
        max_length=120
    )
    food_security = models.CharField(
        _("Food security"),
        max_length=255
    )
    image = models.ImageField(
        _("Image"),
        upload_to='preforms'
    )

    class TranslatableMeta:
        fields = [
            'raw_materials',
            'application',
            'logo',
            'manufacturing_technology',
            'food_security'
        ]

    class Meta:
        verbose_name = _('Bottle Cap')
        verbose_name_plural = _('Bottle Caps')
