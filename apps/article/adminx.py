# author: GongJichao
# createTime: 2020/6/16 11:00
import xadmin
from .models import Article, Category, Tag


class ArticleAdmin(object):
    list_display = ['title', 'excerpt', 'author', 'category', 'tags', 'views']
    style_fields = {"content": "ueditor"}


class CategoryAdmin(object):
    list_display = ['name', 'create_time', 'update_time']


class TagAdmin(object):
    list_display = ['name', 'create_time', 'update_time']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
