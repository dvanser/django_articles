from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Article(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()
    titleEn = models.CharField(max_length=200)
    titleDe = models.CharField(max_length=200)
    contentEn = RichTextUploadingField()
    contentDe = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = ProcessedImageField(upload_to='media/', options={'quality': 80}, blank=False)
    thumbnail = ImageSpecField(processors=[ResizeToFit(200, 200)], options={'quality': 70})

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.slug
