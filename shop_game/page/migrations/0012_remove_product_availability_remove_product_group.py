# Generated by Django 4.1.2 on 2022-11-05 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_alter_product_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
    ]
