from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from members.filters import MemberFilter
from members.models import Member, Classification
from members.serializers import MemberSerializer, ClassificationSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class MemberViewSet(viewsets.ModelViewSet):
    """
    实验室成员
    """
    queryset = Member.objects.filter(is_deleted=0).all()
    serializer_class = MemberSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = MemberFilter
    filter_fields = ('category_name',)  # 筛选


class ClassificationViewSet(viewsets.ModelViewSet):
    """
    成员分类
    """
    queryset = Classification.objects.filter(is_deleted=0).all()
    serializer_class = ClassificationSerializer
