# Generated by Django 3.2.7 on 2021-11-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flora_poblacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poblacion_historica', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('flora', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zonas.flora_zona')),
            ],
        ),
        migrations.CreateModel(
            name='Fauna_poblacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poblacion_historica', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateField()),
                ('fauna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zonas.fauna_zona')),
            ],
        ),
    ]
