# Generated by Django 2.2.13 on 2020-10-30 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0022_auto_20201030_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='travel_reimbursement',
        ),
        migrations.AlterField(
            model_name='application',
            name='is_adult',
            field=models.BooleanField(choices=[(True, 'Agree')], default=None, verbose_name='Please confirm you are 18 or older.'),
        ),
    ]