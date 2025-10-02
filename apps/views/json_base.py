import json
from pathlib import Path

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pagination import CustomPagination

BASE_DIR = Path(__file__).resolve().parent
JSON_DIR = BASE_DIR.parent / "jsons"


class JsonListAPIView(APIView):
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filename = None
    filter_field = "value"

    def get(self, request, *args, **kwargs):
        if not self.filename:
            return Response({"detail": "Filename not set"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        file_path = JSON_DIR / self.filename
        if not file_path.exists():
            return Response({"detail": f"{file_path} topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict) and len(data) == 1:
            values = list(data.values())[0]
        elif isinstance(data, list):
            values = data
        else:
            values = []

        filter_value = request.query_params.get(self.filter_field)
        if filter_value:
            values = [
                item for item in values
                if str(item.get(self.filter_field, "")).lower() == filter_value.lower()
            ]

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(values, request, view=self)
        return paginator.get_paginated_response(page)
