# Generated by Django 4.0.6 on 2022-08-02 16:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='contentDe',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='contentEn',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='contentEn'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='titleDe',
            field=models.CharField(default='titleDe', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='titleEn',
            field=models.CharField(default='titleEn', max_length=200),
            preserve_default=False,
        ),
    ]
