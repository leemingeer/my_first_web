from django.conf.urls import patterns, include, url
from view import hello, blog
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello),
    url(r'^blog/$', blog),
)
