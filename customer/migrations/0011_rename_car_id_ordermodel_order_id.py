# Generated by Django 4.2.1 on 2025-01-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_ordermodel_car_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='car_id',
            new_name='order_id',
        ),
    ]
