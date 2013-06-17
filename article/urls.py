from django.conf.urls import patterns, include, url
from api import ArticleResource

article_resource = ArticleResource()

urlpatterns = patterns('',
                       url('^all/$', 'article.views.articles'),
                       url('^get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url('^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
                       url('^create/$', 'article.views.create'),
                       url('^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
                       url('^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
                       url('^search/$', 'article.views.search_title'),
                       url('^api/$', include(article_resource.urls)),
                       )
