# Generated by Django 3.2.8 on 2021-10-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_lot_lot_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_author',
            field=models.CharField(max_length=64),
        ),
    ]
