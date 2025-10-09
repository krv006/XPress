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
    filter_field = None        # 🔹 bitta filter uchun
    filter_fields = None       # 🔹 bir nechta filter uchun

    def get_json_data(self):
        """JSON faylni o‘qib, list qaytaradi"""
        if not self.filename:
            raise ValueError("filename aniqlanmagan (set qilinmagan)")

        file_path = JSON_DIR / self.filename
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} topilmadi")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict) and len(data) == 1:
            data = list(data.values())[0]
        elif not isinstance(data, list):
            data = []

        return data

    def apply_filters(self, request, data):
        """Bir yoki bir nechta filterlarni qo‘llaydi (case-insensitive, substring qidiruv)"""
        # 🔹 1) Bir nechta filter_fields mavjud bo‘lsa
        if self.filter_fields:
            for field in self.filter_fields:
                value = request.query_params.get(field)
                if value:
                    data = [
                        item for item in data
                        if str(item.get(field, "")).lower().find(value.lower()) != -1
                    ]

        # 🔹 2) Aks holda — bitta filter_field ishlatiladi
        elif self.filter_field:
            value = request.query_params.get(self.filter_field)
            if value:
                data = [
                    item for item in data
                    if str(item.get(self.filter_field, "")).lower().find(value.lower()) != -1
                ]

        return data

    def get_paginated_response(self, data):
        """Paginatsiyani DRF formatida qaytaradi"""
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(data, self.request, view=self)
        return paginator.get_paginated_response(page)

    def get(self, request, *args, **kwargs):
        """Asosiy GET endpoint"""
        self.request = request
        try:
            data = self.get_json_data()
        except FileNotFoundError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data = self.apply_filters(request, data)
        return self.get_paginated_response(data)
