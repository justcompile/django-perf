from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_perf.views.home', name='home'),
    # url(r'^django_perf/', include('django_perf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'store/(?P<store_id>\d+)', 'core.views.store', name='store'),
    url(r'orders(?P<store_id>\d+)?', 'core.views.orders', name='orders')
)
