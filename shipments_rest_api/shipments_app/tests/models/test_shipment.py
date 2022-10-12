from django.test import TestCase
from shipments_app.models import Shipment


class ShipmentTests(TestCase):
    VALID_SHIPMENT_DATA = {
            "shipment_ref": "300",
            "delivery_date": "12.12.2018",
            "delivery_town": "Pazardjik",
            "bayer": "Simeon Iliev",
            "seller": "Ivan Nikolov",
            "status": "In progress",
            "description": "Some simple description"
    }

    def test_deliver_information_expect_success(self):
        shipment = Shipment(**self.VALID_SHIPMENT_DATA)
        self.assertEqual(
            f"Deliver information: From: {self.VALID_SHIPMENT_DATA['seller']}, to {self.VALID_SHIPMENT_DATA['bayer']} is in status: In progress",
            shipment.deliver_information()
        )

