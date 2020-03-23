# encoding: utf-8

import xadmin
from xadmin import views
from .models import *


class ProjectAdmin(object):
    list_display = ["name", "leader", "create_time"]


class ProApproveAdmin(object):
    list_display = ["project", "user", "status"]


class FundAdmin(object):
    list_display = ["project", "purpose", "status", "money"]


xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(ProApprove, ProApproveAdmin)
xadmin.site.register(Fund, FundAdmin)
