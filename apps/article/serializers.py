# author: gongjichao
# createTime: 2020/6/16 11:02

from rest_framework import serializers
from .models import Article, Category, Tag


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章
    """

    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    文章
    """

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    文章
    """

    class Meta:
        model = Tag
        fields = '__all__'
