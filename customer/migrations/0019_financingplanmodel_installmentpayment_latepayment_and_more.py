# Generated by Django 4.2.1 on 2025-01-12 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0018_rentalordermodel_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancingPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years', models.PositiveIntegerField(verbose_name='عدد السنوات')),
                ('interest_rate', models.FloatField()),
                ('max_duration_months', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('late', 'Late')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LatePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('late_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resolved', models.BooleanField(default=False)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.installmentpayment')),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_months', models.PositiveIntegerField()),
                ('monthly_installment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.carmodel')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='العميل')),
                ('financing_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.financingplanmodel')),
            ],
        ),
        migrations.AddField(
            model_name='installmentpayment',
            name='installment_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.installmentrequestmodel'),
        ),
    ]
