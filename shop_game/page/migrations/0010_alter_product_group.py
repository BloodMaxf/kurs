# Generated by Django 4.1.2 on 2022-11-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Shooter', 'Shooter'), ('RPG', 'RPG'), ('Horror', 'Horror'), ('SoulsLike', 'SoulsLike')], default='RPG', max_length=50),
        ),
    ]
