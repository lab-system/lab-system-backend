# author: gongjichao
# createTime: 2020/6/16 11:01
from rest_framework import routers

from article.views import ArticleViewSet, CategoryViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'tag', TagViewSet, basename='tag')

urlpatterns = router.urls
