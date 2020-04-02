# author: GongJichao
# createTime: 2020/4/1 10:26
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from reports.models import WeekReport
from reports.serializers import ReportSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class ReportViewSet(viewsets.ModelViewSet):
    """
    list:
    周报列表
    create:
    写周报
    """
    queryset = WeekReport.objects.filter(is_deleted=0).order_by('-create_time').all()
    pagination_class = DefaultPagination
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data['owner'] = user.id
        ret = super().create(request, *args, **kwargs)
        return ret
