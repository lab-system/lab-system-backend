# author: GongJichao
# createTime: 2020/4/12 11:28

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'attendence', AttendenceViewSet, basename='attendence')

urlpatterns = router.urls