# Create your models here.

from django.db import models
import datetime


class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    memo = models.CharField('MEMO', max_length=1024, blank=True)
    # registered_time = models.DateTimeField('REGISTERED_TIME', null=True, blank=True)
    registered_time = models.DateTimeField('REGISTERED_TIME', default=datetime.datetime.now, null=True, blank=True)

    def __str__(self):
        return self.title