from django.conf.urls import include, url
from rest_framework import routers
from .views import FooListView, FooDetailView, FooViewSet


router = routers.DefaultRouter()
router.register(r'foos', FooViewSet)
urlpatterns = [
    url(r'^foos/(?P<slug>[-\w]+)/$',
        FooDetailView.as_view(), name='foo-detail'),
    url(r'^$', FooListView.as_view(), name='foo-list'),
    url(r'api/', include(router.urls)),
]
