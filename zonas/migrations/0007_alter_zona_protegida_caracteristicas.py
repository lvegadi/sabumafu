# Generated by Django 3.2.7 on 2021-11-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0006_zona_protegida_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona_protegida',
            name='caracteristicas',
            field=models.TextField(),
        ),
    ]
