import os

from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from utils.custom_base_model import BaseModel


def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    # filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    filename = '{}.{}'.format('avatar', ext)
    return os.path.join('avatar', instance.name, filename)


class Classification(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '成员分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Member(BaseModel):
    """
    科研队伍
    """
    MEMBER_TYPE = (
        ('teacher', '导师'),
        ('student', '学生'),
    )

    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    name = models.CharField('名称', help_text='名称', max_length=128, null=True, blank=True)
    birthday = models.DateField("出生年月", help_text="出生年月", null=True, blank=True)
    age = models.IntegerField('年龄', help_text="年龄", null=True, blank=True)
    gender = models.CharField('性别', help_text="性别", max_length=6, choices=GENDER_CHOICES, default="male")
    phone = models.CharField('电话', help_text="电话", null=True, blank=True, max_length=11)
    email = models.EmailField('邮箱', help_text="邮箱", max_length=100, null=True, blank=True)
    member_type = models.CharField("成员类型", help_text="成员类型", max_length=16, choices=MEMBER_TYPE, default=MEMBER_TYPE[1])
    # 一对多
    category = models.ForeignKey(Classification, verbose_name='成员分类', on_delete=models.CASCADE)
    member_title = models.CharField('成员头衔', help_text='成员头衔', max_length=128, null=True, blank=True)
    avatar = ProcessedImageField(verbose_name="头像", help_text='头像', upload_to=user_avatar_path,
                                 default='avatar/default.jpg', processors=[ResizeToFill(120, 120)],
                                 format='JPEG', options={'quality': 60}, null=True, blank=True)
    introduction = models.TextField('介绍', help_text='介绍', null=True, blank=True)
    member_id = models.AutoField('索引', help_text='索引', primary_key=True)

    class Meta:
        verbose_name = "科研队伍"
        verbose_name_plural = verbose_name
        ordering = [
            '-create_time', 'name']

    def __str__(self):
        return self.name
