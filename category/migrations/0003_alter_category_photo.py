# Generated by Django 5.0.2 on 2024-02-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Educational_modules/category/photo', verbose_name='Фото'),
        ),
    ]
