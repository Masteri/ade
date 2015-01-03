from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from news import views
from news.views import news_list, NewsList, SimpleStaticView, SnewsViewSet



router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = patterns('',
    # Examples:

    url(r'^sni/$', news_list, name='news-list'),
    url(r'^ind/', SimpleStaticView.as_view(template_name='index.html')),

    #url(r'^/us/', LisatCreateAPIView.as_view(model=News), name='user-list'),
    url(r'^123/', 'news.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^news/', include('news.urls')),
    #url(r'^api/news/$', 'post_collection'),
	
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

