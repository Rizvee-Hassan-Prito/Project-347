# Generated by Django 4.0.5 on 2022-07-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_account_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='image',
            new_name='profile_pics',
        ),
    ]
