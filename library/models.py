from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="书名", max_length=127)
    desc = models.TextField(verbose_name='介绍', null=True, blank=True)
    publish_time = models.DateTimeField(verbose_name="出版时间", null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    isbn = models.CharField(verbose_name="isbn码", max_length=127, null=True, blank=True)
    score = models.FloatField(verbose_name="评分", null=True, blank=True)
    cover_img = models.ImageField(upload_to='cover/%Y/%m/%d', default='default.jpg',
                                  verbose_name='封面图', null=True, blank=True)
    stock = models.IntegerField(verbose_name="库存", null=True, blank=True)
    review = models.IntegerField(verbose_name="评论数", null=True, blank=True)
    status = models.IntegerField(verbose_name="状态", default=0)

    publisher = models.ForeignKey('Publisher', verbose_name='出版社', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey('Author', verbose_name='作者', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    作者数据模型,包含ID和作者名
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="作者名", max_length=127)
    desc = models.TextField(verbose_name='介绍', null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """
    出版社数据模型,包含ID和出版社名
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127)
    desc = models.TextField(verbose_name='介绍', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    储存文章的分类信息
    文章表的外键指向
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('类名', max_length=127)
    desc = models.TextField(verbose_name='介绍', null=True, blank=True)

    class Meta:
        db_table = "category"
        ordering = ['name']

    def __str__(self):
        return self.name
