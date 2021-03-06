# Generated by Django 3.0.7 on 2020-06-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200618_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='ألتعليق'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='البريد الإلكتروني'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='ألاسم'),
        ),
    ]
