from django.conf.urls import patterns, url, include
from finalweb.views import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^references/(?P<id>.+?)/$', SingleReferenceView.as_view(), name='reference_id'),
                       url(r'^references/$', ReferencesView.as_view(), name='reference'),
                       url(r'^contact/$', ContactView.as_view(), name='contact'),
                       url(r'^questions/$', QuestionsView.as_view(), name='questions'),
                       url(r'^materials/$', MaterialsView.as_view(), name='materials'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
