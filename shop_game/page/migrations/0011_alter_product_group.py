# Generated by Django 4.1.2 on 2022-11-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Shooter', 'Shooter'), ('RPG', 'RPG'), ('SoulsLike', 'SoulsLike'), ('Adventure', 'Adventure'), ('Horror', 'Horror')], default=None, max_length=50),
        ),
    ]
