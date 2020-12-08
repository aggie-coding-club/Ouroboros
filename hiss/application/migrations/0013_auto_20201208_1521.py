# Generated by Django 2.2.13 on 2020-12-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20201107_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='has_team',
            field=models.CharField(choices=[('HT', 'I do have a team'), ('HNT', 'I do not have a team')], max_length=16, verbose_name='Do you have a team yet?'),
        ),
        migrations.AlterField(
            model_name='application',
            name='wants_team',
            field=models.CharField(choices=[('WT', 'I would like you to make me a team'), ('DWT', 'I would not like for you to make me a team')], help_text='We will take into account many factors to make sure you are paired with a team that works well', max_length=16, verbose_name='Would you like to be contacted to help get a team?'),
        ),
    ]
