# Generated by Django 5.0.4 on 2025-02-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_alter_service_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
