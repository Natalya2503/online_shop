# Generated by Django 4.2 on 2024-08-25 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_card',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_on_get',
        ),
        migrations.RemoveField(
            model_name='order',
            name='requires_delivery',
        ),
    ]
