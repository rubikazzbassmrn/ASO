# Generated by Django 2.1.15 on 2020-06-26 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.Status', verbose_name='Estatus'),
        ),
    ]
