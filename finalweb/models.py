from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import MaxValueValidator, MinValueValidator
import os


class Quote(models.Model):
    quote = models.CharField(max_length=300, null=True, blank=True)
    quote_author = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.quote)


class Reference(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    complexity = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(99)])
    newest = models.BooleanField(default=False)

    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    time = models.CharField(max_length=1000, null=True, blank=True)
    customer = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    def save(self, *args, **kwargs):
        if self.newest:
            try:
                temp = Reference.objects.get(newest=True)
                if self != temp:
                    temp.newest = False
                    temp.save()
            except Reference.DoesNotExist:
                pass
        super(Reference, self).save(*args, **kwargs)


def get_file_path(instance, filename):
    return os.path.join('static/img/', filename)


class RefImages(models.Model):
    reference = models.ForeignKey(Reference, null=True, blank=True)
    file = models.ImageField(upload_to=get_file_path, null=True, blank=True)