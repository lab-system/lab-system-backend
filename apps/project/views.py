from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from project.models import Project, ProApprove, Fund
from project.serializers import ProjectSerializer, ProApproveSerializer, FundSerializer, CreateOrUpdateProjectSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class ProJectViewset(viewsets.ModelViewSet):
    """
    list:
        项目列表
    retrieve:
        获取项目详情
    create:
        创建项目
    """
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Project.objects.filter(is_deleted=0).all()
    pagination_class = DefaultPagination
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateOrUpdateProjectSerializer
        return ProjectSerializer


class ProApproveViewSet(viewsets.ModelViewSet):
    """
    项目和成员对应表
    """
    queryset = ProApprove.objects.filter(is_deleted=0).all()
    serializer_class = ProApproveSerializer


class FundViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    资金申请
    """
    queryset = Fund.objects.filter(is_deleted=0).all()
    serializer_class = FundSerializer








