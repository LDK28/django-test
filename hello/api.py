from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from hello.models import TestModel
from hello.serializers import TestSerializer
from hello.filters import TestFilter


class TestApi(ReadOnlyModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    # filter_class = TestFilter