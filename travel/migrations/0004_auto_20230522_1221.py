# Generated by Django 3.2.18 on 2023-05-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_travelplan_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='caption',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
