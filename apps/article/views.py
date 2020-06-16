from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from article.models import Article, Tag, Category
from article.serializers import ArticleSerializer, CategorySerializer, TagSerializer


class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000


class ArticleViewSet(viewsets.ModelViewSet):
    """
    项目和成员对应表
    """
    queryset = Article.objects.filter(is_deleted=0).all()
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    项目和成员对应表
    """
    queryset = Category.objects.filter(is_deleted=0).all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    项目和成员对应表
    """
    queryset = Tag.objects.filter(is_deleted=0).all()
    serializer_class = TagSerializer
