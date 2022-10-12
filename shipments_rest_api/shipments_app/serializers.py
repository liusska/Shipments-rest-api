from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ("id", "shipment_ref", "delivery_date", "delivery_town", "bayer", "seller", "status", "description")