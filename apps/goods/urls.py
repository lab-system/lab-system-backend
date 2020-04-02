from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'good', GoodViewSet, basename='good')
router.register(r'goodborrow', GoodBorrowViewSet, basename='goodborrow')

urlpatterns = router.urls
