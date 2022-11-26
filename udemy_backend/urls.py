from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet

# IMPORTAR BIBLIOTECA QUE NOS RETORNA AUTH TOKEN
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'list', ListViewSet, basename=list) 
router.register(r'item', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
