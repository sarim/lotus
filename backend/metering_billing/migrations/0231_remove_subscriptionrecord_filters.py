# Generated by Django 4.0.5 on 2023-03-18 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0230_auto_20230318_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionrecord',
            name='filters',
        ),
    ]