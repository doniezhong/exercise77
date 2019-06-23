# -*- coding: utf-8 -*-
import base64
import os

from django.conf import settings
from django.http import StreamingHttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception
import qrcode as qr


def home(request):
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')


def qrcode(request):
    return render_mako_context(request, '/home_application/qrcode.html')


def generate_qrcode(request):
    img = qr.make(request.GET.get('url') or 'http://www.baidu.com')
    save_path = os.path.join(settings.MEDIA_ROOT, 'qr.png')
    img.save(save_path)
    with open(save_path, 'rb') as f:
        img_content = f.read()

    return success_result({'img': base64.b64encode(img_content)})


def download_qrcode(request):
    img = open(os.path.join(settings.MEDIA_ROOT, 'qr.png'), 'rb')
    res = FileResponse(img, content_type='application/octet-stream')
    res['Content-Type'] = 'application/octet-stream'
    res['Content-Disposition'] = 'attachment;filename="qr.png"'
    return res


def test(request):
    username = request.user.username
    return success_result(username)


@try_exception('查询业务')
def search_business(request):
    client = get_client_by_request(request)
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
    }
    res = client.cc.search_business(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])



