# Generated by Django 5.1 on 2024-09-01 20:35

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_alter_post_content_alter_post_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]