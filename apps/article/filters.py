# author: gongjichao
# createTime: 2020/7/1 16:05
import django_filters

from article.models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章的过滤类
    """
    category_name = django_filters.CharFilter(method='catogory_name_filter')
    tags_name = django_filters.CharFilter(method='tags_name_filter')

    def catogory_name_filter(self, queryset, name, value):
        return queryset.filter(category__name=value).all()

    def tags_name_filter(self, queryset, name, value):
        return queryset.filter(tags__name=value).all()

    class Meta:
        model = Article
        fields = ['category_name', 'tags_name']
