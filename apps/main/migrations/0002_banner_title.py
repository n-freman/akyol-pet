# Generated by Django 4.2.4 on 2023-09-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.TextField(default=' ', verbose_name='Is Banner Active'),
            preserve_default=False,
        ),
    ]
