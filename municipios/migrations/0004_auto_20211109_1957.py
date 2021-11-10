# Generated by Django 3.2.7 on 2021-11-10 00:57

from django.db import migrations, models
import municipios.models


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0003_auto_20211109_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad_reguladora',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=municipios.models.image_upload_handler),
        ),
        migrations.AlterField(
            model_name='ong',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=municipios.models.image_upload_handler),
        ),
    ]