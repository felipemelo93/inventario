# Generated by Django 5.1 on 2024-09-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_rename_nombre_bodega_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
