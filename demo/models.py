from django.db import models
from django.utils.html import format_html

from qiniu_fields import QiniuFileField


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    img_url = QiniuFileField(prefix='banner', file_type='image', verbose_name='图片')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.title

    def banner_img(self):
        return format_html('<img src="{}" style="height: 45px;"/>', self.img_url)
    banner_img.short_description = u'图片'
    banner_img.allow_tags = True

    class Meta:
        app_label = 'demo'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'
