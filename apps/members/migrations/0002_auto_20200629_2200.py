# Generated by Django 2.2.10 on 2020-06-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, help_text='年龄', null=True, verbose_name='年龄'),
        ),
    ]