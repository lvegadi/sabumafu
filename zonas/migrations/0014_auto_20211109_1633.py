# Generated by Django 3.2.7 on 2021-11-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0013_auto_20211109_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='fauna',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/fauna/'),
        ),
        migrations.AddField(
            model_name='flora',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/flora/'),
        ),
        migrations.AlterField(
            model_name='zona_protegida',
            name='geojson',
            field=models.FileField(blank=True, null=True, upload_to='geojson/'),
        ),
        migrations.AlterField(
            model_name='zona_protegida',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/zonas/'),
        ),
    ]