# -*- coding: utf-8 -*-
import xadmin
import xadmin.views as xviews
from xadmin.layout import Main, Fieldset, Side

from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(xviews.BaseAdminView, BaseSetting)


class AdminSettings(object):
    global_search_models = [Banner]
    site_title = 'QiniuFields'
    site_footer = 'QiniuFields Inc. 2017'
    menu_style = 'default'  # accordion

    def get_site_menu(self):
        return (
            {'title': '内容管理', 'menus': (
                {'title': 'Banner', 'icon': 'fa fa-gift', 'url': self.get_model_url(Banner, 'changelist')},
            )},
        )

xadmin.site.register(xviews.CommAdminView, AdminSettings)


class BannerAdmin(object):
    list_display = ('title', 'banner_img', 'created_time')
    search_fields = ['title']
    form_layout = (
        Main(Fieldset(u'基本信息', 'title', 'img_url')),
        Side(Fieldset(u'其他信息', 'created_time', 'updated_time'))
    )
    readonly_fields = ('created_time', 'updated_time')


xadmin.site.register(Banner, BannerAdmin)
