from django.conf.urls.defaults import *
from django.contrib import admin
from django.shortcuts import render
import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r"^$", render, {"template_name" : "home.html"}, "home"),
    (r"^contact/$", "burgercom.views.handle_contact", {}, "contactus"),
    (r"^people/$", 
        render, {
			"template_name" : "people.html", 
			"dictionary" : {"section" : "people"}
		}, "people"
    ),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

