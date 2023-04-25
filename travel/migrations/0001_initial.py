# Generated by Django 3.2.18 on 2023-04-25 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('activities', models.CharField(blank=True, choices=[('HIKING', 'Hiking'), ('SNOWBOARDIND', 'Snowboarding'), ('CYCLING', 'Cycling'), ('MOUNTAIN BIKING', 'Mountain biking'), ('SWIMMING', 'Swimming'), ('CAMPING', 'Camping'), ('ROAD TRIPS', 'Road trips'), ('EXPLORING', 'Exploring'), ('PHOTOGRAPHY', 'Photography')], max_length=80)),
                ('image', models.ImageField(blank=True, default='../https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', upload_to='images/')),
                ('approved', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]