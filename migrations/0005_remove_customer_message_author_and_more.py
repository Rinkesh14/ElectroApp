# Generated by Django 4.2.3 on 2024-02-26 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electro_app', '0004_customer_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='customer_request',
            name='connect',
        ),
        migrations.RemoveField(
            model_name='review',
            name='boss',
        ),
        migrations.DeleteModel(
            name='subscriber',
        ),
        migrations.DeleteModel(
            name='customer_message',
        ),
        migrations.DeleteModel(
            name='customer_request',
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
