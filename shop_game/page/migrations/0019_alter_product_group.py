# Generated by Django 4.1.2 on 2022-12-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Shooter', 'Shooter'), ('Adventure', 'Adventure'), ('SoulsLike', 'SoulsLike'), ('Horror', 'Horror'), ('RPG', 'RPG')], default='RPG', max_length=20),
        ),
    ]