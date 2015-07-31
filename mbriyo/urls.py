from django.conf.urls import patterns, include, url
from django.contrib import admin

from mbriyo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mbriyo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.WelcomePage, name='home'),
)
