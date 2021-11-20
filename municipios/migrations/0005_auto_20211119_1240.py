# Generated by Django 3.2.7 on 2021-11-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '0004_auto_20211109_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad_municipio',
            name='entidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='municipios.entidad_reguladora'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entidad_municipio',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='municipios.municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='municipio',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='municipios.departamento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ong_municipio',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='municipios.municipio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ong_municipio',
            name='ong',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='municipios.ong'),
            preserve_default=False,
        ),
    ]