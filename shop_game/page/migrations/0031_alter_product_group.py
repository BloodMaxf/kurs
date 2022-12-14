# Generated by Django 4.1.2 on 2022-12-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0030_remove_product_availability_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Shooter', 'Shooter'), ('SoulsLike', 'SoulsLike'), ('Horror', 'Horror'), ('RPG', 'RPG'), ('Adventure', 'Adventure')], default='RPG', max_length=20),
        ),
    ]