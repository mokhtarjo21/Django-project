# Generated by Django 4.2.1 on 2025-01-08 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_ordermodel_car_rental_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='buy_car_order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.buycarordermodel', verbose_name='مودل طلب شراء السيارة'),
        ),
    ]
