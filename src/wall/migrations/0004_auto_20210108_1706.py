# Generated by Django 3.1.4 on 2021-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Пост'),
        ),
    ]
