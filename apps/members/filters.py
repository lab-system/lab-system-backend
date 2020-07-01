# author: gongjichao
# createTime: 2020/7/1 16:05
import django_filters

from article.models import Article
from members.models import Member


class MemberFilter(django_filters.rest_framework.FilterSet):
    """
    成员的过滤类
    """
    category_name = django_filters.CharFilter(method='catogory_name_filter')

    def catogory_name_filter(self, queryset, name, value):
        return queryset.filter(category__name=value).all()

    class Meta:
        model = Member
        fields = ['category_name']
