# Generated by Django 4.1.2 on 2022-10-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_product_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body',
            field=models.TextField(default=None),
        ),
    ]
