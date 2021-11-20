# Generated by Django 3.2 on 2021-11-19 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('booking_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='block_days', to='listings.bookinginfo')),
            ],
        ),
    ]
