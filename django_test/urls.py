from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    url(r'^articles/', include('article.urls')),

    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url('^article/$', include('article.urls')),
                        url('^accounts/login/$', 'django_test.views.login'),
                        url('^accounts/auth/$', 'django_test.views.auth_view'),
                        url('^accounts/loggedin/$', 'django_test.views.loggedin'),
                        url('^accounts/invalid/$', 'django_test.views.invalid_login'),
                        url('^accounts/logout/$', 'django_test.views.logout'),
                        url('^accounts/register/$', 'django_test.views.register'),
                        url('^accounts/register_success/$', 'django_test.views.register_success'),
                        )
