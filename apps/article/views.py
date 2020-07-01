from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from article.filters import ArticleFilter
from article.models import Article, Tag, Category
from article.serializers import ArticleSerializer, CategorySerializer, TagSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class ArticleViewSet(viewsets.ModelViewSet):
    """
    文章
    """
    queryset = Article.objects.filter(is_deleted=0).all()
    serializer_class = ArticleSerializer

    filter_backends = (DjangoFilterBackend,)
    # todo: 以下两种过滤方式都可以
    filter_class = ArticleFilter
    # filter_fields = ('category__name', 'tags__name') #筛选


class CategoryViewSet(viewsets.ModelViewSet):
    """
    分类
    """
    queryset = Category.objects.filter(is_deleted=0).all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    标签
    """
    queryset = Tag.objects.filter(is_deleted=0).all()
    serializer_class = TagSerializer
