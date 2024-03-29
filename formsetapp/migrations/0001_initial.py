# Generated by Django 2.2.4 on 2019-08-30 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_addr', models.CharField(max_length=30)),
                ('cust_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_menu', models.CharField(max_length=20)),
                ('order_quantity', models.CharField(max_length=3)),
                ('order_price', models.CharField(max_length=5)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formsetapp.Customer')),
            ],
        ),
    ]
