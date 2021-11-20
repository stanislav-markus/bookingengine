# Generated by Django 3.2 on 2021-11-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_rename_blockdays_blockday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockday',
            name='booking_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='block_days', to='listings.bookinginfo'),
        ),
    ]