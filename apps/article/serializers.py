# author: gongjichao
# createTime: 2020/6/16 11:02

from rest_framework import serializers
from .models import Article, Category, Tag


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章
    """
    firstImg = serializers.CharField(label='文章图片', help_text='文章图片', required=False)
    category_name = serializers.CharField(label='文章分类', help_text='文章分类', required=False, source='category.name')
    tags_name = serializers.CharField(label='文章标签', help_text='文章标签', required=False, source='tags.name')

    def to_representation(self, instance):
        self.firstImg = instance.get_content_img_url
        instance.firstImg = self.firstImg
        ret = super().to_representation(instance)
        return ret

    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    分类
    """

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    标签
    """

    class Meta:
        model = Tag
        fields = '__all__'
