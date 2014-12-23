from django.conf import settings
from django.conf.urls import patterns, url
from tennis_app import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # url(r'^register?$', 'tennis_app.views.register', name='register'),
        # url(r'^login?$', 'tennis_app.views.login', name='login'),


)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )