# Generated by Django 4.1.2 on 2022-11-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_remove_product_availability_remove_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genre',
            field=models.CharField(default='', max_length=30),
        ),
    ]
