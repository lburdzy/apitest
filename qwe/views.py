from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Foo


class FooListView(ListView):
    model = Foo


class FooDetailView(DetailView):
    model = Foo
