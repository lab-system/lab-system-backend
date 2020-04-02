from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from goods.models import Good, GoodBorrow
from goods.serializers import GoodsSerializer, GoodBorrowSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class GoodViewSet(viewsets.ModelViewSet):
    """
    list:
    显示物品列表
    """
    queryset = Good.objects.filter(is_deleted=0).all()
    pagination_class = DefaultPagination
    serializer_class = GoodsSerializer


class GoodBorrowViewSet(viewsets.ModelViewSet):
    """
    list:
    显示物品借用
    """
    queryset = GoodBorrow.objects.filter(is_deleted=0).all()
    pagination_class = DefaultPagination
    serializer_class = GoodBorrowSerializer
