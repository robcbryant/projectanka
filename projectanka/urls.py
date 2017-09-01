

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

#from maqluengine.admin import admin_site

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    url(r'', include('maqluengine.urls')),     
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
