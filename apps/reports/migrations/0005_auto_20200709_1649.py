# Generated by Django 2.2.10 on 2020-07-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20200629_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekreport',
            name='week_count',
            field=models.IntegerField(default=19, help_text='周次', verbose_name='周次'),
        ),
    ]