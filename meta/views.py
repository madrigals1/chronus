from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from config import constants


class CustomPagination(PageNumberPagination):
    page_size = constants.PAGINATION_PAGE_SIZE
    page_size_query_param = "page_size"
    max_page_size = 100


class CustomModelViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if not hasattr(self, "serializer_classes"):
            return self.serializer_class

        if self.action in ["list", "retrieve"]:
            return self.serializer_classes["read_only"]

        return self.serializer_classes["default"]
