# Generated by Django 4.1.2 on 2022-11-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_product_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]