# Generated by Django 3.2.8 on 2021-11-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='active',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
