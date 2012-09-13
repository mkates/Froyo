from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('cablefinder.views',
    # Examples:
    # url(r'^$', 'cable.views.home', name='home'),
    #url(r'^cable/', include('cable.foo.urls')),
	
	url(r'^$', 'index'),
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
