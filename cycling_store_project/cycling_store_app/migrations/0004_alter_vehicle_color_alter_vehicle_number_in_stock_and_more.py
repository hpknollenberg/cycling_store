# Generated by Django 5.0.6 on 2024-05-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_store_app', '0003_alter_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_in_stock',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
