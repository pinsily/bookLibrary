import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from library.models import Book
from library.templatetags.paginate_tags import getpages
from users.models import UserProfile, BorrowRecord


def index(request):
    book_list = Book.objects.filter(status=0)
    pages, book_list = getpages(request, book_list, 9)
    return render(request, 'library/book_list.html', locals())


def borrow_status(user, book):
    if not isinstance(user, UserProfile):
        print("未登录, 返回未借书")
        return False

    # 有无未还的书籍
    record = BorrowRecord.objects.filter(user=user, book=book, is_return=0).first()
    if record:
        return True
    else:
        return False


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    if not book:
        print("书籍不存在")
        redirect(reverse('library:index'))

    is_borrow = borrow_status(request.user, book)

    cate_books = Book.objects.filter(status=0).filter(category=book.category).filter(~Q(id=book_id))[:3]

    return render(request, 'library/book-detail.html', locals())


def borrow_book(request, book_id):
    user = request.user
    if not isinstance(user, UserProfile):
        print("未登录, 不能借书")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))

    book = Book.objects.get(id=book_id)
    if not book:
        print("书籍不存在, 不能借书")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))

    record = BorrowRecord.objects.filter(user=user, book=book, is_return=0).first()
    if record:
        print("该书已借, 不能再借")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))

    # 生成借书记录 十天后应还
    should_time = datetime.datetime.now() + datetime.timedelta(days=10)
    BorrowRecord.objects.create(user=user, book=book, should_time=should_time)

    print("借书成功")
    return redirect(reverse('library:detail', kwargs={"book_id": book_id}))


def return_book(request, book_id):
    user = request.user
    if not isinstance(user, UserProfile):
        print("未登录, 不能还书")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))
    book = Book.objects.get(id=book_id)
    if not book:
        print("书籍不存在, 不能还书")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))
    record = BorrowRecord.objects.filter(user=user, book=book, is_return=0).first()
    if not record:
        print("没有未还记录, 不能还书")
        return redirect(reverse('library:detail', kwargs={"book_id": book_id}))
    record.is_return = 1
    record.save()
    return redirect(reverse('library:detail', kwargs={"book_id": book_id}))


def my_book(request):
    """
    我的已借书籍

    :param request:
    :return:
    """
    user = request.user
    if not isinstance(user, UserProfile):
        print("未登录, 无个人页面")
        return redirect(reverse('library:index'))
    record_list = BorrowRecord.objects.filter(user=user, is_return=0)

    pages, record_list = getpages(request, record_list, 9)
    return render(request, 'library/my_book.html', locals())
