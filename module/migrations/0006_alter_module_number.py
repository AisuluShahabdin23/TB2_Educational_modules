# Generated by Django 4.2.10 on 2024-02-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_alter_module_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Порядковый номер'),
        ),
    ]