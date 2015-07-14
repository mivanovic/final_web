__author__ = 'marko'

from django.conf import settings
from finalst import secret_settings


def constants(request):
    return {
        'JQUERY_VERSION': settings.JQUERY_VERSION,
        'GOOGLE_ANALYTICS_ID': secret_settings.GOOGLE_ANALYTICS_ID,
        'BOOTSTRAP_VERSION': settings.BOOTSTRAP_VERSION,
        'RESPOND_VERSION': settings.RESPOND_VERSION,
        'LAZYLOAD_VERSION': settings.LAZYLOAD_VERSION,

        'MOBILE_PHONE': settings.MOBILE_PHONE,
        'PHONE': settings.PHONE,
        'FAX_PHONE': settings.FAX_PHONE,
    }