import os

from django.db import models

from users.models import UserProfile
from utils.custom_base_model import BaseModel
from DjangoUeditor.models import UEditorField
from django.template.defaultfilters import striptags
from pyquery import PyQuery


# 图片上传路径
# def article_img_path(instance, filename):
#     ext = filename.split('.')[-1]
#     # filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
#     filename = '{}.{}'.format('article_img', ext)
#     return os.path.join('article', instance.username, filename)


class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name #

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = models.CharField('标题', max_length=70)

    content = UEditorField('文章内容', height=500, width=1000, default=u'', imagePath='ueditor/images/',
                        filePath='ueditor/files/', upload_settings={"imageMaxSize": 1204000}, settings={},
                        command=None)

    # 文章摘要，默认可以为空值
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 一对多
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    # 一对多
    tags = models.ForeignKey(Tag, verbose_name='标签', null=True, blank=True, on_delete=models.CASCADE)

    # 文章作者
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)

    # 统计文章阅读量
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = [
            '-create_time']  # ordering = ['-created_time', 'title'] 表示首先依据 created_time 排序，如果 created_time 相同，则再依据 title 排序

    # 访问文章，阅读量统计方法
    # 这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # # 重写父类的save逻辑，在每次更新时，自动填写更新时间
    # def save(self, *args, **kwargs):
    #     self.content.
    #
    #     # 如果摘要没有手动输入，自动获取前54个字符
    #     if not self.excerpt:
    #         md = markdown.Markdown(extensions={
    #             'markdown.extensions.extra',
    #             'markdown.extensions.codehilite',
    #         })
    #
    #         # strip_tags,删除markdown转化成html后的html标签
    #         self.excerpt = strip_tags(md.convert(self.body))[:54] + '……'
    #
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # 获取后台文本编辑器图文内容中图片 url 地址
    def get_content_img_url(self):
        temp = Article.objects.filter(pk=str(self.id)).values('content')  # values 获取 Article 数据表中的 content 字段内容
        html = PyQuery(temp[0]['content'])  # pq 方法获取编辑器 html 内容
        # print(html, "\n", "----")
        img_path = PyQuery(html)('img').attr('src')  # 截取 html 内容中的路径
        # print("pic", img_path)
        return img_path  # 返回第一张图片路径
