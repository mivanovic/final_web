from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
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
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    thumbnail = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    def create_thumbnail(self):
        thumb_width = 400
        thumb_height = 400

        django_type = self.image.file.content_type

        if django_type == 'image/jpeg':
            pil_type = 'jpeg'
            file_extension = 'jpg'
        elif django_type == 'image/png':
            pil_type = 'png'
            file_extension = 'png'

        image = Image.open(StringIO(self.image.read()))

        src_width, src_height = image.size
        src_ratio = float(src_width) / float(src_height)
        dst_ratio = float(thumb_width) / float(thumb_height)

        if dst_ratio < src_ratio:
            crop_height = src_height
            crop_width = crop_height * dst_ratio
            x_offset = int(float(src_width - crop_width) / 2)
            y_offset = 0
        else:
            crop_width = src_width
            crop_height = crop_width / dst_ratio
            x_offset = 0
            y_offset = int(float(src_height - crop_height) / 3)

        image = image.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
        image = image.resize((thumb_width, thumb_height), Image.ANTIALIAS)

        temp_handle = StringIO()
        image.save(temp_handle, pil_type)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type=django_type)
        self.thumbnail.save('{}_thumbnail.{}'.format(os.path.splitext(suf.name)[0], file_extension), suf, save=False)

    def save(self, *args, **kwargs):
        self.create_thumbnail()
        force_update = False

        if self.id:
            force_update = True

        super(RefImages, self).save(force_update=force_update)