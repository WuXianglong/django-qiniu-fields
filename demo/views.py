#! -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from . import qiniu_utils


@login_required
def get_qiniu_token(request):
    return JsonResponse({'uptoken': qiniu_utils.get_token()})
