# Generated by Django 2.2.10 on 2020-06-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
    ]