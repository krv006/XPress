from django.db.models import Model
from django.db.models.fields import CharField


class VehicleMake(Model):
    value = CharField(max_length=255)

    def __str__(self):
        return self.value


class VehicleModel(Model):
    value = CharField(max_length=255)

    def __str__(self):
        return self.value



class VehicleYear(Model):
    value = CharField(max_length=255)

    def __str__(self):
        return self.value