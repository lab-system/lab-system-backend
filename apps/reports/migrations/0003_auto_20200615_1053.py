# Generated by Django 2.2.10 on 2020-06-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200401_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekreport',
            name='week_count',
            field=models.IntegerField(default=16, help_text='周次', verbose_name='周次'),
        ),
    ]