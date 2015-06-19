from django.conf.urls import patterns, url, include
from finalweb.views import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view()),
                       url(r'^references/(?P<id>.+?)/$', SingleReferenceView.as_view()),
                       url(r'^references/$', ReferencesView.as_view()),
                       url(r'^contact/send/$', SendMail.as_view()),
                       url(r'^contact/$', ContactView.as_view()),

                       url(r'^admin/', include(admin.site.urls)),
                       )
