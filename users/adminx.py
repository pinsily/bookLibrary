import xadmin
from . import models


class UserProfileAdmin(object):
    # 要列出的字段
    list_display = ('id', 'username', 'email', 'is_active',)
    # 可以搜索的字段
    search_fields = ('name',)
    # 列出可以编辑的字段
    list_editable = ('gender', 'location',)
    # 右侧过滤条件
    list_filter = ()
    # icon
    model_icon = "fa fa-group"
    # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
    relfield_style = 'fk-ajax'
    ordering = ['id']
    # 后台可选刷新频率
    refresh_times = [3, 5]


xadmin.site.unregister(models.UserProfile)
xadmin.site.register(models.UserProfile, UserProfileAdmin)
