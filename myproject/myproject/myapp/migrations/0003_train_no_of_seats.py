# Generated by Django 4.2.5 on 2023-11-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_ticket_date_of_journey_train_source_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='no_of_seats',
            field=models.IntegerField(default=50),
        ),
    ]
