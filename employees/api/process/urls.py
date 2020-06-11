from django.urls import include, path
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns
from api.process.api_v1.rest import views


# ModelViewset urls
router = routers.DefaultRouter(trailing_slash=True)
router.register(r'process_list', views.ProcessViewset, basename='proclist')
router.register(r'process_mainid', views.ProcessMainidViewset, basename='procmain')
router.register(r'process_subpoint', views.ProcessSubpointViewset, basename='procsubpt')
router.register(r'connection', views.ConnectionsViewset, basename='connection')
router.register(r'repeat_task', views.RepeatTaskViewset, basename='repeat')
router.register(r'regular_task', views.RegularTaskViewset, basename='regulartask')



urlpatterns = router.urls

