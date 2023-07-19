# Generated by Django 4.2.2 on 2023-07-18 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0006_remove_order_food_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webkiosk.food'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CustomerOrder',
        ),
    ]
