from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from translations.models import Translatable


class Preform(models.Model):
    code = models.CharField(
        _("code"), 
        max_length=16, 
        primary_key=True
    )
    thread_standard = models.CharField(
        _("Thread standard"),
        max_length=120
    )
    weight = models.FloatField(
        _("Weight"),
        null=True,
        blank=True
    )
    height = models.FloatField(
        _("Height"),
        null=True,
        blank=True
    )
    blown_volume = models.CharField(
        _("Blown volume"),
        max_length=120,
        null=True
    )
    image = models.ImageField(
        _("Image"),
        upload_to='preforms'
    )

    class Meta:
        verbose_name = _('Preform')
        verbose_name_plural = _('Preforms')
    
    def get_absolute_url(self):
        return reverse('preforms-detail', kwargs={'pk': self.code})
    
    def __str__(self):
        return self.code


class BottleCap(Translatable):
    code = models.CharField(
        _("code"), 
        max_length=16,
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

    def get_absolute_url(self):
        return reverse('bottlecap-detail', kwargs={'pk': self.code})
    
    def __str__(self):
        return self.code
