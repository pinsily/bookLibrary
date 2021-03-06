# Generated by Django 2.2.20 on 2021-05-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210521_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.IntegerField(blank=True, null=True, verbose_name='评论数'),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Author', verbose_name='作者'),
        ),
    ]
