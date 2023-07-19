# Generated by Django 4.2.2 on 2023-07-18 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0005_alter_order_orderdatetime_alter_order_paymentmode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webkiosk.order')),
            ],
        ),
    ]
