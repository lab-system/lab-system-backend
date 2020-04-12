from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from attendence.models import Attendence
from attendence.serializers import AttendenceSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class AttendenceViewSet(viewsets.ModelViewSet):
    """
    list:
    签到列表
    """
    queryset = Attendence.objects.filter(is_deleted=0).all()
    pagination_class = DefaultPagination
    serializer_class = AttendenceSerializer


