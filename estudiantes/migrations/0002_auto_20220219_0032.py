# Generated by Django 2.2.26 on 2022-02-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primer_parcial',
            name='calif_expo_1er',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='primer_parcial',
            name='calif_mono',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='primer_parcial',
            name='participacion_1er',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
