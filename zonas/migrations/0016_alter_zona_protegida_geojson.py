# Generated by Django 3.2.7 on 2021-11-10 00:40

from django.db import migrations, models
import zonas.models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0015_auto_20211109_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona_protegida',
            name='geojson',
            field=models.FileField(blank=True, null=True, upload_to=zonas.models.geojson_upload_handler),
        ),
    ]