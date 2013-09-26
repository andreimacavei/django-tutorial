from django.conf.urls import patterns, include, url
from mysite.books import views, models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    url(r'^hello/$', 'hello'),
    url(r'^$', 'home'),
    url(r'^time/$', 'current_datetime'),
    url(r'^time/plus/(?P<h>\d{1,2})/$', 'hours_ahead'),
    url(r'^meta/$', 'display_meta'),
    url(r'^login/$', 'user_login'),
    url(r'^login/success/$', 'login_success'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^book/$', views.objects_list, {'model': models.Book}),
    url(r'^search/$', views.search),
    url(r'^author/$', views.objects_list, {'model': models.Author}),
)

urlpatterns += patterns('mysite.contact.views',
    url(r'^contact/$', 'contact'),
    url(r'^contact/thanks/$', 'success'),
)
