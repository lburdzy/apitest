from django.conf.urls import url

from .views import FooListView, FooDetailView

urlpatterns = [
    url(r'^foos/(?P<slug>[-\w]+)/$',
        FooDetailView.as_view(), name='foo-detail'),
    url(r'^$', FooListView.as_view(), name='foo-list'),
]
