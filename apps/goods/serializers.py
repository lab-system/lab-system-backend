from rest_framework import serializers

from goods.models import Good, GoodBorrow
from users.models import UserProfile
from users.serializers import UserDetailSerializer


class GoodsSerializer(serializers.ModelSerializer):
    """
    物品列表
    """
    active_num = serializers.IntegerField(label='可借数量', read_only=True, required=False, help_text='可借数量')
    user_borrowed = UserDetailSerializer(many=True, required=False)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        self.active_num = instance.active_num
        return ret

    class Meta:
        model = Good
        fields = '__all__'


class GoodBorrowSerializer(serializers.ModelSerializer):
    """
    物品借用表
    """
    good_name = serializers.CharField(label='物品名称', help_text='物品名称', read_only=True, required=False, source='good.name')
    user_name = serializers.CharField(label='使用者', help_text='使用者', read_only=True, required=False, source='user.cname')

    class Meta:
        model = GoodBorrow
        fields = '__all__'

