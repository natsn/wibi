from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from project import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'note', views.VideoNoteViewSet)
router.register(r'level', views.LevelViewSet)
router.register(r'error', views.ErrorViewSet)
router.register(r'star', views.StarViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'pagevisit', views.PageVisitViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'section', views.SectionViewSet)
router.register(r'page', views.PageViewSet)
router.register(r'edge', views.EdgeViewSet)
router.register(r'permission', views.PermissionViewSet)
router.register(r'media', views.PermissionViewSet)
router.register(r'tip', views.TipViewSet)
router.register(r'custompage', views.CustomPageViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'response', views.ResponseViewSet)

urlpatterns = patterns('',
	url(r'^api/tip/(?P<id>[0-9]+)', 'project.views.tip', name='tip'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', 'project.views.home', name='home'),
)