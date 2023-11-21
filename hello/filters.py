from django_filters import rest_framework as filters

from hello.models import TestModel

class TestFilter(filters.FilterSet):
    class Meta:
        model = TestModel
        fields = ('string')