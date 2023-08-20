from django.db import models
from translations.models import Translatable


class Preform(models.Model):
    code = models.IntegerField(primary_key=True)
    thread_standard = models.CharField(max_length=120)
    weight = models.IntegerField()
    height = models.FloatField(null=True)
    blown_volume = models.FloatField()
    image = models.ImageField(upload_to='preforms')

    class Meta:
        verbose_name = 'Preform'
        verbose_name_plural = 'Preforms'


class BottleCap(Translatable):
    code = models.IntegerField(primary_key=True)
    raw_materials = models.CharField(max_length=120)
    application = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    manufacturing_technology = models.CharField(max_length=120)
    food_security = models.CharField(max_length=255)
    image = models.ImageField(upload_to='preforms')

    class TranslatableMeta:
        fields = [
            'raw_materials',
            'application',
            'logo',
            'manufacturing_technology',
            'food_security'
        ]

    class Meta:
        verbose_name = 'Bottle Cap'
        verbose_name_plural = 'Bottle Caps'
