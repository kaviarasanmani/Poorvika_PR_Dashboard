# Generated by Django 4.0.8 on 2022-12-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill_of_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_code', models.CharField(max_length=255)),
                ('material_type', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('material_price', models.CharField(max_length=255)),
            ],
        ),
    ]
