# Generated by Django 4.1.3 on 2022-12-04 07:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_loginuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='user_profile_image'),
        ),
    ]
