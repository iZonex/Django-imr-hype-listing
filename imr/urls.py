from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'listing.views.premium'),
    #url(r'^listing/$', 'listing.views.premium'),
    url(r'^listing/(?P<name>[\w|\W]+)/$', 'listing.views.detail'),
    url(r'^imperavi/', include('imperavi.urls')),
    url(r'^accounts/', include('registration.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'', include('social_auth.urls')),
)
