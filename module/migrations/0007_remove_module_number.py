# Generated by Django 4.2.10 on 2024-02-22 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0006_alter_module_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='number',
        ),
    ]
