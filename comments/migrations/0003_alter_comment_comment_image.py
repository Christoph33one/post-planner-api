# Generated by Django 3.2.18 on 2023-05-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_image',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/dqgs0kltd/image/upload/v1673026764/samples/ecommerce/accessories-bag.jpg', upload_to='images/'),
        ),
    ]