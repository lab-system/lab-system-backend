#  认证中间件


import re
import logging
from django.http.response import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from users.models import Url

logger = logging.getLogger('views')


class AuthMiddleware(MiddlewareMixin):
    '''
    登录验证
    '''
    def process_request(self, request):
        while_url_list = Url.objects.filter(user_type='anonymous').values_list('url', flat=True)
        for url in while_url_list:
            if re.match(url, request.path_info): return None
        user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))
        print('request', request)
        print('jwt', user_jwt)
        if user_jwt is not None:
            user = user_jwt[0]
            request.user = user
            return None
        response = JsonResponse({'detail': 'Permission denied'})
        response.status_code = 403
        return response

class UrlCheckMiddleware(MiddlewareMixin):
    """
    验证用户URL访问权限
    """
    def urlcheck(self, request, queryset):
        for instance in queryset:
            method = instance.method
            if method == 'ALL': method = request.method
            if method != request.method: continue
            if re.match(instance.url, request.path_info): return True
        return False

    def process_request(self, request):
        anonymous_url_queryset = Url.objects.filter(user_type='anonymous')
        authenticated_url_queryset = Url.objects.filter(user_type='authenticated')
        # 匿名用户基础权限
        if self.urlcheck(request, anonymous_url_queryset): return None
        if not request.user.is_authenticated: return None
        user = request.user
        # 登录用户基础权限
        if self.urlcheck(request, authenticated_url_queryset): return None
        # 自定义用户权限
        role_list = user.roles.all()
        print('role_list', role_list)
        for role in role_list:
            url_obj_list = role.urls.all()
            if self.urlcheck(request, url_obj_list): return None
        response = JsonResponse({'detail': 'Permission denied'})
        response.status_code = 403
        return response