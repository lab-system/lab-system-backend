# author: GongJichao
# createTime: 2020/6/29 19:39
import xadmin
from members.models import Member, Classification


class MemberAdmin(object):
    list_display = ['name', 'age', 'gender', 'phone', 'email', 'member_type', 'category', 'introduction']


class ClassificationAdmin(object):
    list_display = ['name', 'create_time', 'update_time']


xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(Classification, ClassificationAdmin)

