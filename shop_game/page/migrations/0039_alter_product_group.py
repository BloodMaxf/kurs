# Generated by Django 4.1.2 on 2022-12-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0038_alter_product_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Horror', 'Horror'), ('Shooter', 'Shooter'), ('Roguelike', 'Roguelike'), ('RPG', 'RPG'), ('Adventure', 'Adventure'), ('SoulsLike', 'SoulsLike')], default='RPG', max_length=20),
        ),
    ]
