from django.db import models


class BaseModel(models.Model):
    """
    模型基类（抽象类）
    """
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', help_text='更新时间', auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField('逻辑删除', default=False, help_text='逻辑删除')

    class Meta:
        abstract = True
        ordering = ['-id']

    def delete(self, using=None, keep_parents=False):
        # super().delete()
        self.is_deleted = True
        self.save()
