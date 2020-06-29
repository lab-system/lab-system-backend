# author: GongJichao
# createTime: 2020/6/29 19:39

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'classify', ClassificationViewSet, basename='classify')

urlpatterns = router.urls
