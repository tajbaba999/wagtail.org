# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 10:44
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    ContentType = apps.get_model("contenttypes.ContentType")

    ContentType.objects.filter(app_label="blog", model="blogindexpage").delete()
    ContentType.objects.filter(app_label="core", model="blogindexpage").update(
        app_label="blog", model="blogindexpage"
    )

    ContentType.objects.filter(app_label="blog", model="blogpage").delete()
    ContentType.objects.filter(app_label="core", model="blogpage").update(
        app_label="blog", model="blogpage"
    )

    ContentType.objects.filter(app_label="blog", model="author").delete()
    ContentType.objects.filter(app_label="core", model="author").update(
        app_label="blog", model="author"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailredirects", "0005_capitalizeverbose"),
        ("wagtailcore", "0028_merge"),
        ("wagtailforms", "0003_capitalizeverbose"),
        ("core", "0031_auto_20160728_1315"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="author",
                    name="image",
                ),
                migrations.RemoveField(
                    model_name="blogindexpage",
                    name="listing_image",
                ),
                migrations.RemoveField(
                    model_name="blogindexpage",
                    name="page_ptr",
                ),
                migrations.RemoveField(
                    model_name="blogindexpage",
                    name="social_image",
                ),
                migrations.RemoveField(
                    model_name="blogpage",
                    name="author",
                ),
                migrations.RemoveField(
                    model_name="blogpage",
                    name="listing_image",
                ),
                migrations.RemoveField(
                    model_name="blogpage",
                    name="main_image",
                ),
                migrations.RemoveField(
                    model_name="blogpage",
                    name="page_ptr",
                ),
                migrations.RemoveField(
                    model_name="blogpage",
                    name="social_image",
                ),
                migrations.DeleteModel(
                    name="Author",
                ),
                migrations.DeleteModel(
                    name="BlogIndexPage",
                ),
                migrations.DeleteModel(
                    name="BlogPage",
                ),
            ],
            database_operations=[],
        ),
    ]
