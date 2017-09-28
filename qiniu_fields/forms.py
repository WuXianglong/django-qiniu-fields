#! -*- coding: utf-8 -*-
from django import forms

from .widgets import QiniuFileWidget, QiniuFileListWidget


class QiniuFileFormField(forms.URLField):
    prefix = ''
    file_type = 'all'
    widget = QiniuFileWidget

    def __init__(self, *args, **kwargs):
        kwargs["widget"] = QiniuFileWidget(attrs={'prefix': self.prefix, 'file_type': self.file_type})
        super(QiniuFileFormField, self).__init__(*args, **kwargs)
