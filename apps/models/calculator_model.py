from django.db.models import DateTimeField, CharField, DateField, Model, DecimalField, EmailField


class ShippingPriceRequest(Model):
    pickup_zip = CharField(max_length=20)
    dropoff_zip = CharField(max_length=20)
    estimated_ship_date = DateField()
    vehicle_type = CharField(max_length=50)
    ship_via_id = CharField(max_length=10)
    vehicle_runs = CharField(max_length=10)
    # tashqi API dan kelgan natija
    calculated_price = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup_zip} -> {self.dropoff_zip} ({self.vehicle_type})"


class Order(Model):
    pickup_zip = CharField(max_length=20)
    dropoff_zip = CharField(max_length=20)
    estimated_ship_date = DateField()
    vehicle_type = CharField(max_length=100)
    ship_via_id = CharField(max_length=10)
    vehicle_runs = CharField(max_length=10)

    calculated_price = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Customer (step2) — boshida bo'sh bo'lishi mumkin
    name = CharField(max_length=255, blank=True, null=True)
    phone_number = CharField(max_length=50, blank=True, null=True)
    email = EmailField(blank=True, null=True)

    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} — {self.pickup_zip} -> {self.dropoff_zip}"
