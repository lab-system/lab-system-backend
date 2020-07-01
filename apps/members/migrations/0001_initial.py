# Generated by Django 2.2.10 on 2020-06-29 21:52

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import members.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '成员分类',
                'verbose_name_plural': '成员分类',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('name', models.CharField(blank=True, help_text='名称', max_length=128, null=True, verbose_name='名称')),
                ('birthday', models.DateField(blank=True, help_text='出生年月', null=True, verbose_name='出生年月')),
                ('age', models.IntegerField(blank=True, help_text='年龄', max_length=16, null=True, verbose_name='年龄')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', help_text='性别', max_length=6, verbose_name='性别')),
                ('phone', models.CharField(blank=True, help_text='电话', max_length=11, null=True, verbose_name='电话')),
                ('email', models.EmailField(blank=True, help_text='邮箱', max_length=100, null=True, verbose_name='邮箱')),
                ('member_type', models.CharField(choices=[('teacher', '导师'), ('student', '学生')], default=('student', '学生'), help_text='成员类型', max_length=16, verbose_name='成员类型')),
                ('member_title', models.CharField(blank=True, help_text='成员头衔', max_length=128, null=True, verbose_name='成员头衔')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, default='avatar/default.jpg', help_text='头像', null=True, upload_to=members.models.user_avatar_path, verbose_name='头像')),
                ('introduction', models.TextField(blank=True, help_text='介绍', null=True, verbose_name='介绍')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Classification', verbose_name='成员分类')),
            ],
            options={
                'verbose_name': '实验室成员',
                'verbose_name_plural': '实验室成员',
                'ordering': ['-create_time', 'name'],
            },
        ),
    ]