# Generated by Django 4.0.4 on 2022-07-28 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='modified_by',
        ),
    ]
