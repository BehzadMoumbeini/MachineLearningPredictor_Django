# Generated by Django 3.2.16 on 2023-01-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Female'), (1, 'Male')], max_length=10, null=True),
        ),
    ]
