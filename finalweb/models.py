from django.db import models
from django.utils.encoding import smart_unicode
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import ugettext_lazy as _
from PIL import Image, ImageOps
from cStringIO import StringIO
import os


class Quote(models.Model):
    quote = models.CharField(max_length=300, null=True, blank=True, verbose_name='Izreka')
    quote_author = models.CharField(max_length=30, null=True, blank=True, verbose_name='Autor')

    class Meta:
        verbose_name = _('Izreka')
        verbose_name_plural = _('Izreke')

    def __unicode__(self):
        return smart_unicode(self.quote)


class Reference(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Naziv')
    complexity = models.PositiveIntegerField(default=0, null=True, blank=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Kompleksnost')
    newest = models.BooleanField(default=False, verbose_name='Najnovije')

    location = models.CharField(max_length=100, null=True, blank=True, verbose_name='Lokacija')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Opis')
    time = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Datum')
    customer = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Narucitelj')

    class Meta:
        verbose_name = _('Referenca')
        verbose_name_plural = _('Reference')

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


def get_file_path(filename):
    return 'static/img/{}'.format(filename)


class RefImages(models.Model):
    reference = models.ForeignKey(Reference, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='Slika')
    thumbnail = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='Minijatura')

    class Meta:
        verbose_name = _('Slika')
        verbose_name_plural = _('Slike')

    def create_thumbnail(self):
        thumb_size = (400, 400)
        django_type = self.image.file.content_type

        if django_type == 'image/jpeg':
            pil_type = 'jpeg'
            file_extension = 'jpg'
        elif django_type == 'image/png':
            pil_type = 'png'
            file_extension = 'png'

        image = Image.open(StringIO(self.image.read()))
        image = ImageOps.fit(image, thumb_size, method=Image.ANTIALIAS)

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


class Questions(models.Model):
    INTERIOR = 'Int'
    EXTERIOR = 'Ext'
    CATEGORIES = (
        (INTERIOR, 'Interijer'),
        (EXTERIOR, 'Eksterijer'),
    )
    question = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Pitanje')
    answer = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Odgovor')
    category = models.CharField(max_length=20, choices=CATEGORIES)

    class Meta:
        verbose_name = _('Pitanje')
        verbose_name_plural = _('Pitanja')

    def __unicode__(self):
        return smart_unicode(self.question)


class Materials(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, verbose_name='Naziv')
    url = models.CharField(max_length=300, null=True, blank=True, verbose_name='Link')
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='Slika')

    def __unicode__(self):
        return smart_unicode(self.name)