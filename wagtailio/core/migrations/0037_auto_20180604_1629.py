# Generated by Django 2.0.6 on 2018-06-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0036_homepagemaincarouselitem_homepagesecondarycarouselitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="call_to_action_internal_link",
        ),
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="image",
        ),
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="page",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="author_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="desktop_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="mobile_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="page",
        ),
        migrations.DeleteModel(
            name="HomePageMainCarouselItem",
        ),
        migrations.DeleteModel(
            name="HomePageSecondaryCarouselItem",
        ),
    ]
