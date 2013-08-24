# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.index'),
    # url(r'^login/$', 'app.views.login_view'),
    # url(r'^logout/$', 'app.views.logout_view'),
    # url(r'^productos/$', 'app.views.productos'),
    # url(r'^productos/(\d+)/$', 'app.views.detalle'),
    # url(r'^productos/(\d+)/comentario/nuevo/$', 'app.views.nuevo_comentario'),
     url(r'^admin/', include(admin.site.urls)),
)
