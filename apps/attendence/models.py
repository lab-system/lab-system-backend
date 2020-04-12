from django.db import models
from django.utils import timezone

from users.models import UserProfile
from utils.custom_base_model import BaseModel


class Attendence(BaseModel):
    """
    签到表
    """

    user = models.ForeignKey(UserProfile, verbose_name='用户', help_text='用户', on_delete=models.CASCADE)
    # cur_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField('签到时间', help_text='签到时间', null=True, blank=True)
    end_time = models.DateTimeField('签退时间', help_text='签退时间', null=True, blank=True)
    duration = models.DecimalField('时长', help_text='时长', max_digits=5, decimal_places=2, default=0)
    date = models.DateField('当前时间', help_text='当前时间', default=timezone.now)
    is_leave = models.BooleanField('是否签退', help_text='是否签退', default=False)
    detail = models.TextField('描述', help_text='描述', default='无')
    leave_count = models.IntegerField('签到次数', help_text='签到次数', default=0)

    def __str__(self):
        return self.user.cname
