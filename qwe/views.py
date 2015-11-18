from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Foo
from rest_framework import viewsets
from .serializers import FooSerializer


class FooListView(ListView):
    model = Foo


class FooDetailView(DetailView):
    model = Foo


class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer
