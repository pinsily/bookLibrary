# Generated by Django 2.2.20 on 2021-05-22 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_status'),
        ('users', '0002_auto_20210521_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('borrow_time', models.DateTimeField(verbose_name='借书时间')),
                ('should_time', models.DateTimeField(verbose_name='应还时间')),
                ('return_time', models.DateTimeField(blank=True, null=True, verbose_name='归还时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.Book', verbose_name='书籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='出版社')),
            ],
            options={
                'db_table': 'borrow_record',
                'ordering': ['-borrow_time'],
            },
        ),
    ]
