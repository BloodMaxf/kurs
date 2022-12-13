# Generated by Django 4.1.2 on 2022-12-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_product_availability_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('RPG', 'RPG'), ('SoulsLike', 'SoulsLike'), ('Shooter', 'Shooter'), ('Horror', 'Horror')], default='RPG', max_length=20),
        ),
    ]
