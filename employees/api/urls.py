from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


schema_view = get_swagger_view(title='Micromerce API')



urlpatterns = [
    path('', include(router.urls)),
    path("employees/docs/", schema_view),
]
