from django.db import models

from users.models import UserProfile
from utils.custom_base_model import BaseModel


class Good(BaseModel):
    """
    实验室物品
    """
    name = models.CharField('名称', help_text='名称', max_length=128)
    price = models.IntegerField('价格', help_text='价格', blank=True)
    all_num = models.IntegerField('数量', help_text='数量', blank=True)
    user_borrowed = models.ManyToManyField(UserProfile, verbose_name='借用者', help_text='借用者', blank=True,
                                           through='GoodBorrow')

    @property
    def active_num(self):
        """
        :return: 可借的数量
        """
        return self.all_num-sum([g.num for g in self.goodborrow_set.all()])

    class Meta:
        ordering = ['-create_time']
        verbose_name = '物品'
        verbose_name_plural = '物品'
        permissions = (
            ("apply_good", u"可以申请物品"),
        )

    def __str__(self):
        return self.name


class GoodBorrow(BaseModel):
    """
    物品借用表
    """
    AUDIT_STATUS = (
        (0, '等待审核'),
        (1, '审核通过'),
        (2, '驳回'),
    )
    good = models.ForeignKey(Good, verbose_name='物品', help_text='物品', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(UserProfile, verbose_name='借用者', help_text='借用者', on_delete=models.CASCADE,
                             blank=True, null=True)
    num = models.IntegerField('数量', help_text='数量', default=1)
    start_t = models.DateField('开始时间', help_text='开始时间', blank=True, null=True)
    end_t = models.DateField('结束时间', help_text='结束时间', blank=True, null=True)
    reject_reason = models.TextField('驳回原因', help_text='驳回原因', blank=True, null=True)
    status = models.IntegerField('借用状态', help_text='借用状态', default=0, choices=AUDIT_STATUS)

    class Meta:
        ordering = ['-good']
