# Generated by Django 4.2.19 on 2025-03-22 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_blog_author_alter_blog_content_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(db_index=True, default=datetime.datetime(2025, 3, 22, 16, 11, 27, 597918), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 22, 16, 11, 27, 597918), verbose_name='Опубликована'),
        ),
    ]
