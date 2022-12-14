# Generated by Django 4.1.2 on 2022-12-14 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0033_alter_product_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased_products',
            name='key',
        ),
        migrations.RemoveField(
            model_name='purchased_products',
            name='title',
        ),
        migrations.AddField(
            model_name='purchased_products',
            name='product_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='page.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Roguelike', 'Roguelike'), ('Horror', 'Horror'), ('Shooter', 'Shooter'), ('Adventure', 'Adventure'), ('RPG', 'RPG'), ('SoulsLike', 'SoulsLike')], default='RPG', max_length=20),
        ),
    ]
