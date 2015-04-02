from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from project import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'project.views.home', name='home'),
    # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
