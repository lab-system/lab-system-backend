# author: GongJichao
# createTime: 2020/4/1 10:26

from rest_framework import serializers

from reports.models import WeekReport
from users.serializers import UserDetailSerializer


class ReportSerializer(serializers.ModelSerializer):

    owner_name = serializers.CharField(label='汇报人姓名', help_text='汇报人姓名', required=False, read_only=True, source='owner.cname')
    current_user = UserDetailSerializer(label='当前用户', help_text='当前用户', required=False, read_only=True)

    def to_representation(self, instance):
        self.current_user = self.context['request'].user
        instance.current_user = self.current_user
        ret = super().to_representation(instance)
        return ret

    class Meta:
        model = WeekReport
        fields = '__all__'
