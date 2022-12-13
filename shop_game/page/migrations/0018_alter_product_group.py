# Generated by Django 4.1.2 on 2022-12-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0017_alter_product_availability_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Adventure', 'Adventure'), ('Horror', 'Horror'), ('Shooter', 'Shooter'), ('RPG', 'RPG'), ('SoulsLike', 'SoulsLike')], default='RPG', max_length=20),
        ),
    ]
