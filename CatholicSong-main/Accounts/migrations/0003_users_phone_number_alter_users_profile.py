# Generated by Django 5.0.3 on 2024-11-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_users_musician_users_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='Profile'),
        ),
    ]