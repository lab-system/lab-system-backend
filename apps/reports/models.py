from django.db import models

from reports.weekformat import get_week_count, get_this_monday, get_this_sunday
from users.models import UserProfile
from utils.custom_base_model import BaseModel

COUNT = get_week_count()


class WeekReport(BaseModel):
    title = models.CharField('周报标题', help_text='周报标题', max_length=100, blank=True)
    content = models.TextField('周报内容', help_text='周报内容')
    owner = models.ForeignKey(UserProfile, verbose_name='所有者', help_text='所有者', on_delete=models.SET_NULL, null=True, blank=True)
    week_count = models.IntegerField('周次', help_text='周次', default=COUNT)
    remark = models.CharField('备注', help_text='备注', max_length=100, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '周报'
        verbose_name_plural = '周报'

    def save(self, *args, **kwargs):
        # 设置周报标题和周次
        self.remark = "第" + str(self.week_count) + "周(" + str(get_this_monday()) + "至" + str(get_this_sunday()) + ")周报"
        super(WeekReport, self).save()
