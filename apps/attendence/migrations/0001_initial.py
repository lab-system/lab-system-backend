# Generated by Django 2.2.10 on 2020-06-15 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('start_time', models.DateTimeField(blank=True, help_text='签到时间', null=True, verbose_name='签到时间')),
                ('end_time', models.DateTimeField(blank=True, help_text='签退时间', null=True, verbose_name='签退时间')),
                ('duration', models.DecimalField(decimal_places=2, default=0, help_text='时长', max_digits=5, verbose_name='时长')),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='当前时间', verbose_name='当前时间')),
                ('is_leave', models.BooleanField(default=False, help_text='是否签退', verbose_name='是否签退')),
                ('detail', models.TextField(default='无', help_text='描述', verbose_name='描述')),
                ('leave_count', models.IntegerField(default=0, help_text='签到次数', verbose_name='签到次数')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
