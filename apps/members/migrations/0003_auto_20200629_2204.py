# Generated by Django 2.2.10 on 2020-06-29 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200629_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-create_time', 'name'], 'verbose_name': '科研队伍', 'verbose_name_plural': '科研队伍'},
        ),
    ]
