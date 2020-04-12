# author: GongJichao
# createTime: 2020/4/12 11:27
from rest_framework import serializers

from attendence.models import Attendence


class AttendenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendence
        fields = '__all__'