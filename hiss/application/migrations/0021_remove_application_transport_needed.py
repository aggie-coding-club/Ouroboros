# Generated by Django 2.2.13 on 2020-10-30 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0020_auto_20201030_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='transport_needed',
        ),
    ]