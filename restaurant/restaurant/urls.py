from django.urls import path
from rest.views import dish_view, dish_pk_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version='v1',
        description="API for managing restaurant menu",
        terms_of_service="https://github.com/opielapatryk/Django_Menu_API",
        contact=openapi.Contact(email="patryk.opiela02@gmail.com"),
        license=openapi.License(name="Patryk Opiela"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/dishes/', dish_view), # list, post, put
    path('api/v1/dishes/<int:pk>', dish_pk_view), # get, patch, delete
]
