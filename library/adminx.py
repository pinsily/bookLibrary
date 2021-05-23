from . import models
import xadmin


class BookAdmin(object):
    # 要列出的字段
    list_display = (
        'id', 'status', 'name', 'desc', 'publish_time', 'isbn', 'score', 'cover_img', "publisher", "author", "category")
    # 可以搜索的字段
    search_fields = ('name', 'status')
    # 列出可以编辑的字段
    list_editable = ('name', 'desc',)
    # 右侧过滤条件
    list_filter = ()
    # icon
    model_icon = "fa fa-group"
    # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
    relfield_style = 'fk-ajax'
    ordering = ['id']
    # 后台可选刷新频率
    refresh_times = [3, 5]


class AuthorAdmin(object):
    # 要列出的字段
    list_display = ('id', 'name', 'desc',)
    # 可以搜索的字段
    search_fields = ('name',)
    # 列出可以编辑的字段
    list_editable = ('name', 'desc',)
    # 右侧过滤条件
    list_filter = ()
    # icon
    model_icon = "fa fa-group"
    # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
    relfield_style = 'fk-ajax'
    ordering = ['id']
    # 后台可选刷新频率
    refresh_times = [3, 5]


class PublisherAdmin(object):
    # 要列出的字段
    list_display = ('id', 'name', 'desc',)
    # 可以搜索的字段
    search_fields = ('name',)
    # 列出可以编辑的字段
    list_editable = ('name', 'desc',)
    # 右侧过滤条件
    list_filter = ()
    # icon
    model_icon = "fa fa-group"
    # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
    relfield_style = 'fk-ajax'
    ordering = ['id']
    # 后台可选刷新频率
    refresh_times = [3, 5]


class CategoryAdmin(object):
    # 要列出的字段
    list_display = ('id', 'name', 'desc',)
    # 可以搜索的字段
    search_fields = ('name',)
    # 列出可以编辑的字段
    list_editable = ('name', 'desc',)
    # 右侧过滤条件
    list_filter = ()
    # icon
    model_icon = "fa fa-group"
    # 下拉框搜索，当有外键指向他时会以ajax方式加载，数据量过大时很有用
    relfield_style = 'fk-ajax'
    ordering = ['id']
    # 后台可选刷新频率
    refresh_times = [3, 5]


xadmin.site.register(models.Author, AuthorAdmin)
xadmin.site.register(models.Publisher, PublisherAdmin)
xadmin.site.register(models.Category, CategoryAdmin)
xadmin.site.register(models.Book, BookAdmin)
