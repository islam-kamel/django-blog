# Generated by Django 3.0.7 on 2020-06-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200621_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
