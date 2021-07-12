# Generated by Django 3.1.1 on 2021-01-16 12:31

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210116_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='defaults/cover_image.jpg', null=True, upload_to=user.models.upload_cover_to),
        ),
    ]
