from drf_spectacular.utils import extend_schema, OpenApiParameter

from apps.views import JsonListAPIView

pagination_params = [
    OpenApiParameter(name="page", description="Sahifa raqami", required=False, type=int),
    OpenApiParameter(name="page_size", description="Har bir sahifadagi elementlar soni (default=12)", required=False,
                     type=int),
]
filter_param = lambda field: [
    OpenApiParameter(name=field, description=f"{field} bo‘yicha filter", required=False, type=str),
]


@extend_schema(tags=["shipping"], parameters=pagination_params + filter_param("value"))
class VehicleMakeAPIView(JsonListAPIView):
    filename = "vehicle_makes.json"
    filter_field = "value"


@extend_schema(tags=["shipping"], parameters=pagination_params + filter_param("value"))
class VehicleModelAPIView(JsonListAPIView):
    filename = "vehicle_models.json"
    filter_field = "value"


@extend_schema(tags=["shipping"], parameters=pagination_params + filter_param("value"))
class VehicleYearAPIView(JsonListAPIView):
    filename = "vehicle_years.json"
    filter_field = "value"


@extend_schema(tags=["shipping"], parameters=pagination_params + filter_param("name"))
class ZipCodeAPIView(JsonListAPIView):
    filename = "zip_codes_full.json"
    filter_field = "name"
