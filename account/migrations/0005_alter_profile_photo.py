# Generated by Django 5.0.6 on 2024-06-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default', upload_to='users/%Y/%m/%d/'),
        ),
    ]
