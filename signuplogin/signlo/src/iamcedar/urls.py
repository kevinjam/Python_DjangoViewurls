from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    #here i declare the url inside my article
    #(r'^articles/', include('article.urls')),
    #this url call the home page of my template here
    #url(r'^$', 'iamcedar.views.home'),
    # url(r'^$', 'iamcedar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #user authetication urls

    #url(r'^accounts/login/$', 'iamcedar.views.login'),
    #url(r'^accounts/auth/$', 'iamcedar.views.auth_view'),
    #url(r'^accounts/logout/$', 'iamcedar.views.logout'),
    #url(r'^accounts/loggedin/$', 'iamcedar.views.loggedin'),
    #url(r'^accounts/invalid/$', 'iamcedar.views.invalid_login'),
)
