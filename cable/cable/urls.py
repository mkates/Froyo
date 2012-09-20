from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()


urlpatterns = patterns('cablefinder.views',
  	#Contact Form URL
	url(r'^contact$','contact'),
	url(r'^$', 'index'),
	#secondary urls
	url(r'^preferences$','preferences'),
	url(r'^findpackage$','findpackage'),
	url(r'^buypackage$','buypackage'),
	
	url(r'^browse$', 'browse'),
	url(r'^question/$','question'),
    #url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    #url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    #url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
