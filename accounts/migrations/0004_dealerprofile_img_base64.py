# Generated by Django 4.2.1 on 2025-01-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_is_dealer_dealerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealerprofile',
            name='img_base64',
            field=models.TextField(null=True),
        ),
    ]
