# Generated by Django 4.1.2 on 2022-12-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0019_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('RPG', 'RPG'), ('Horror', 'Horror'), ('SoulsLike', 'SoulsLike'), ('Shooter', 'Shooter'), ('Adventure', 'Adventure')], default='RPG', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('key', 'title')},
        ),
    ]