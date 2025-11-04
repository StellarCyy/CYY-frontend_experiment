from django.shortcuts import render
import os
from django.http import Http404
from django.template import TemplateDoesNotExist
import json
import datetime
# Create your views here.
PAGE_CONFIGS = {
    'index': {
        'title': '首页 - 我的网站',
        'meta_description': '欢迎访问我的网站',
        'meta_keywords': '首页,欢迎',
        'meta_author': '网站管理员',
    },
    'test1': {
        'title': '实验页面',
        'meta_description': '无名光神物种',
        'meta_keywords': '无名光神物种',
        'meta_author': '我',
    },
}
def get_client_ip(request):
    """获取客户端 IP 地址"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def index(request):
    context = {
        'title': '首页 - 我的网站',
        'meta_description': '欢迎访问我的网站',
        'meta_keywords': '首页,欢迎',
        'meta_author': '网站管理员',
    }
    return render(request,'index.html',context)


def universal_page(request, page_name):
    clean_name = page_name.rstrip('/').replace('.html', '')
    template_name = f'{clean_name}.html'

    context = PAGE_CONFIGS.get(clean_name, {
        'title': f'{clean_name} - 我的网站',
        'meta_description': f'这是{clean_name}页面的描述',
        'meta_keywords': clean_name,
        'meta_author': '网站管理员',
    })
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input:
            print(f"🎯 用户提交内容: {user_input}")
            print(f"📱 来自页面: {clean_name}")
            print(f"📍 用户IP: {get_client_ip(request)}")
            context['submitted_data'] = user_input
    try:
        return render(request, template_name, context)
    except TemplateDoesNotExist:
        raise Http404(f"页面 '{clean_name}' 不存在")
