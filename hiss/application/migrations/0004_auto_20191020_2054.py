# Generated by Django 2.2.4 on 2019-10-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20191018_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='question3',
            field=models.TextField(max_length=500, verbose_name="What is a cool prize you'd like to win at TAMUhack?"),
        ),
        migrations.AlterField(
            model_name='application',
            name='transport_needed',
            field=models.CharField(choices=[('drive', 'Driving'), ('th-bus', 'TAMUhack Bus'), ('fly', 'Flying'), ('public', 'Public Transportation'), ('walk-cycle', 'Walking/Biking')], max_length=11),
        ),
    ]
