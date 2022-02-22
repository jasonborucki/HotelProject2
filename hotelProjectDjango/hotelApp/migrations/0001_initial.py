# Generated by Django 4.0.2 on 2022-02-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adults', models.FloatField()),
                ('repeated_guest', models.FloatField()),
                ('hotel_type', models.FloatField()),
                ('direct_binary', models.FloatField()),
                ('children', models.FloatField()),
                ('babies', models.FloatField()),
                ('cancellations_binary', models.FloatField()),
                ('uncanceled_binary', models.FloatField()),
                ('booking_changes', models.FloatField()),
                ('waiting_list', models.FloatField()),
                ('required_parking', models.FloatField()),
                ('special_requests', models.FloatField()),
                ('average_rate', models.FloatField()),
                ('lead_time', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]
