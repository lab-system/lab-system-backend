# author: GongJichao
# createTime: 2020/6/29 19:39
from rest_framework import serializers

from members.models import Member, Classification


class ClassificationSerializer(serializers.ModelSerializer):
    """
    成员分类
    """

    class Meta:
        model = Classification
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    """
    实验室成员
    """
    category_name = serializers.CharField(label='成员分类', help_text='成员分类', required=False, source='category.name')

    class Meta:
        model = Member
        fields = '__all__'



