from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户类
    """
    phone = models.CharField(max_length=20, verbose_name='手机', blank=True, null=True)

    def __str__(self):
        return self.username


class BorrowRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("UserProfile", verbose_name='出版社', on_delete=models.DO_NOTHING)
    book = models.ForeignKey('library.Book', verbose_name='书籍', on_delete=models.DO_NOTHING)
    borrow_time = models.DateTimeField(verbose_name="借书时间", auto_now_add=True)
    should_time = models.DateTimeField(verbose_name="应还时间",)
    return_time = models.DateTimeField(verbose_name="归还时间", blank=True, null=True)
    is_return = models.IntegerField(verbose_name="是否归还", default=0)

    class Meta:
        db_table = 'borrow_record'
        ordering = ['-borrow_time']


