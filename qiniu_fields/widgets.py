#! -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.html import smart_urlquote


class QiniuFileWidget(forms.URLInput):
    input_type = 'file'
    template_name = 'file.html'

    def __init__(self, attrs=None):
        final_attrs = {
            'domain': settings.QINIU_DOMAIN,
            'uptoken_url': settings.QINIU_UPTOKEN_URL,
        }
        if attrs is not None:
            final_attrs.update(attrs)
        super(QiniuFileWidget, self).__init__(attrs=final_attrs)

    def get_context(self, name, value, attrs):
        context = super(QiniuFileWidget, self).get_context(name, value, attrs)
        context['current_label'] = '当前：'
        context['widget']['href'] = smart_urlquote(context['widget']['value']) if value else ''
        return context

    @property
    def media(self):
        return forms.Media(js=('qiniu_fields/plupload/plupload.full.min.js', 'qiniu_fields/plupload/i18n/zh_CN.js',
                               'qiniu_fields/qiniu/qiniu.min.js', 'qiniu_fields/qiniu/ui.min.js'))

    # class Media:
    #     js = ('qiniu_fields/plupload/plupload.full.min.js', 'qiniu_fields/plupload/i18n/zh_CN.js',
    #           'qiniu_fields/qiniu/qiniu.min.js', 'qiniu_fields/qiniu/ui.min.js')


class QiniuFileListWidget(forms.Textarea):
    template_name = 'file_list.html'

    def __init__(self, attrs=None):
        final_attrs = {
            'domain': settings.QINIU_DOMAIN,
            'uptoken_url': settings.QINIU_UPTOKEN_URL,
        }
        if attrs is not None:
            final_attrs.update(attrs)
        super(QiniuFileListWidget, self).__init__(attrs=final_attrs)

    @property
    def media(self):
        return forms.Media(js=('qiniu_fields/plupload/plupload.full.min.js', 'qiniu_fields/plupload/i18n/zh_CN.js',
                               'qiniu_fields/qiniu/qiniu.min.js', 'qiniu_fields/qiniu/ui.min.js'))

    # class Media:
    #     js = ('qiniu_fields/plupload/plupload.full.min.js', 'qiniu_fields/plupload/i18n/zh_CN.js',
    #           'qiniu_fields/qiniu/qiniu.min.js', 'qiniu_fields/qiniu/ui.min.js')
