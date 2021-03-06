# Generated by Django 2.2.13 on 2020-11-07 23:27

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0011_auto_20201107_1706"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="address",
            field=address.models.AddressField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="address.Address",
            ),
        ),
    ]
