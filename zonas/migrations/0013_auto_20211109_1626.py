# Generated by Django 3.2.7 on 2021-11-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0012_auto_20211107_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alerta',
            old_name='usuario_id',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='zona_protegida',
            name='geojson_url',
        ),
        migrations.RemoveField(
            model_name='zona_protegida',
            name='image_url',
        ),
        migrations.AddField(
            model_name='zona_protegida',
            name='geojson',
            field=models.FileField(null=True, upload_to='geojson/'),
        ),
        migrations.AddField(
            model_name='zona_protegida',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
