# Generated by Django 2.2.10 on 2020-06-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20200615_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekreport',
            name='week_count',
            field=models.IntegerField(default=18, help_text='周次', verbose_name='周次'),
        ),
    ]
