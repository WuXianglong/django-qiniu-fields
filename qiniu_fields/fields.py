#! -*- coding: utf-8 -*-
from django.db import models

from .widgets import QiniuFileWidget, QiniuFileListWidget
from .forms import QiniuFileFormField


class QiniuFileField(models.URLField):
    widget_clz = QiniuFileWidget
    form_field_clz = QiniuFileFormField

    def __init__(self, verbose_name=None, name=None, prefix='', file_type='all', **kwargs):
        self.prefix = prefix
        self.file_type = file_type
        kwargs['max_length'] = 500
        super(QiniuFileField, self).__init__(verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        self.form_field_clz.prefix = self.prefix
        self.form_field_clz.file_type = self.file_type
        kwargs.update({
            'form_class': self.form_field_clz,
            'widget': self.widget_clz(attrs={'prefix': self.prefix, 'file_type': self.file_type})
        })
        return super(QiniuFileField, self).formfield(**kwargs)


class QiniuFileListField(models.TextField):

    def __init__(self, *args, prefix='', file_type='all', **kwargs):
        self.prefix = prefix
        self.file_type = file_type
        super(QiniuFileListField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.update({
            'widget': QiniuFileListWidget(attrs={'prefix': self.prefix, 'file_type': self.file_type}),
        })
        return super(QiniuFileListField, self).formfield(**kwargs)
