from django.db.models import Q
from rest_framework import serializers

from users.models import UserProfile
from users.serializers import UserDetailSerializer
from .models import Project, ProApprove, Fund


class ProjectSerializer(serializers.ModelSerializer):
    """
    项目管理
    """
    leader_id = serializers.IntegerField(label='负责人id', help_text='负责人id', source='leader.id')
    leader_name = serializers.CharField(label='负责人', help_text='负责人', required=False, source='leader.cname')
    # users = serializers.PrimaryKeyRelatedField(label="用户", help_text="用户", many=True,
    #                                            queryset=UserProfile.objects.filter(is_active=True).order_by('-id'))
    users = UserDetailSerializer(many=True, required=False)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret

    def to_internal_value(self, data):
        dd = super().to_internal_value(data)
        return dd

    # def validate(self, attrs):
    #     name = attrs['name']
    #     if Project.objects.filter(name=name).count(): raise serializers.ValidationError("该项目已存在")

    class Meta:
        model = Project
        fields = '__all__'


class CreateOrUpdateProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(label="用户", help_text="用户", many=True,
                                               queryset=UserProfile.objects.filter(is_active=True).order_by('-id'))

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        print('vdata%s' % validated_data)
        users = validated_data.pop('users')
        project = Project.objects.create(**validated_data)
        for user in users:
            ProApprove.objects.create(project=project, user=user, status=0)
        return project

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data['leader'] = validated_data['leader'].id
        users = validated_data.pop('users')
        self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        # 更新m2m中间表
        users_id_list = []
        for user in users:
            users_id_list.append(user.id)
            if ProApprove.objects.filter(Q(project_id=instance.id) & Q(user_id=user.id)).count() == 0:
                ProApprove.objects.create(project=instance, user=user, status=0)

        user_list = ProApprove.objects.filter(project_id=instance.id).values_list('user', flat=True)
        del_list = list(set(user_list).difference(set(users_id_list)))
        for item in del_list:
            ProApprove.objects.filter(Q(project_id=instance.id) & Q(user_id=item)).delete()
        return instance



class ProApproveSerializer(serializers.ModelSerializer):
    """
    审核
    """

    class Meta:
        model = ProApprove
        fields = '__all__'


class FundSerializer(serializers.ModelSerializer):
    """
    资金申请
    """
    class Meta:
        model = Fund
        fields = '__all__'
