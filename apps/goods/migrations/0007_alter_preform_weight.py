# Generated by Django 4.2.4 on 2023-09-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_squashed_0006_alter_bottlecap_code_alter_preform_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preform',
            name='weight',
            field=models.CharField(blank=True, null=True, verbose_name='Weight'),
        ),
    ]
