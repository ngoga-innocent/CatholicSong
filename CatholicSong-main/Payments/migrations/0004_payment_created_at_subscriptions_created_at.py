# Generated by Django 5.0.3 on 2024-11-02 16:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0003_payment_reference_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]