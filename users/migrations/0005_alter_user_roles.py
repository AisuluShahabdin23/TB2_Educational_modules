# Generated by Django 5.0.2 on 2024-02-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(blank=True, choices=[('teacher', 'teacher'), ('moderator', 'moderator')], max_length=15, null=True),
        ),
    ]
