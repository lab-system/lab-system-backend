# Generated by Django 2.2.10 on 2020-03-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200324_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cname',
            field=models.CharField(blank=True, help_text='姓名', max_length=30, null=True, verbose_name='姓名'),
        ),
    ]
