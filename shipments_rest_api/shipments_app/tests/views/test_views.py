import json
from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client

from shipments_app.models import Shipment
from shipments_app.serializers import ShipmentSerializer

client = Client()


class ShipmentTests(TestCase):
    def setUp(self):
        self.first_shipment = Shipment.objects.create(
            shipment_ref="300", delivery_date="12.12.2018", delivery_town="Pazardjik", bayer="Simeon Iliev", seller="Ivan Nikolov", status="In progress", description="Some simple description")
        self.second_shipment = Shipment.objects.create(
            shipment_ref="299", delivery_date="1.1.2023", delivery_town="Vidin", bayer="Peter Petrov", seller="Nikolay Nikolov", status="In progress", description="Some simple description")
        self.third_shipment = Shipment.objects.create(
            shipment_ref="298", delivery_date="12.11.2018", delivery_town="Sofia", bayer="Kosta Kostov", seller="Kristyan Pavlov", status="In progress", description="Some simple description")

    VALID_SHIPMENT_DATA = {
        "shipment_ref": "300",
        "delivery_date": "12.12.2018",
        "delivery_town": "Pazardjik",
        "bayer": "Simeon Iliev",
        "seller": "Ivan Nikolov",
        "status": "In progress",
        "description": "Some simple description"
    }

    INVALID_SHIPMENT_DATA = {
        "shipment_ref": "",
        "delivery_date": "12.12.2018",
        "delivery_town": "Pazardjik",
        "bayer": "Simeon Iliev",
        "seller": "Ivan Nikolov",
        "status": "In progress",
        "description": "Some simple description"
    }

    def test_shipment_create_expect_success(self):
        shipment = Shipment(**self.VALID_SHIPMENT_DATA)

        self.assertEqual(self.VALID_SHIPMENT_DATA['shipment_ref'], shipment.shipment_ref)
        self.assertEqual(self.VALID_SHIPMENT_DATA['delivery_date'], shipment.delivery_date)
        self.assertEqual(self.VALID_SHIPMENT_DATA['delivery_town'], shipment.delivery_town)
        self.assertEqual(self.VALID_SHIPMENT_DATA['bayer'], shipment.bayer)
        self.assertEqual(self.VALID_SHIPMENT_DATA['seller'], shipment.seller)
        self.assertEqual(self.VALID_SHIPMENT_DATA['status'], shipment.status)
        self.assertEqual(self.VALID_SHIPMENT_DATA['description'], shipment.description)

    def test_all_shipments(self):
        response = client.get(reverse('shipments list'))
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_shipment(self):
        response = client.get(reverse('shipment details', kwargs={'id': self.first_shipment.pk}))
        shipment = Shipment.objects.get(id=self.first_shipment.pk)
        serializer = ShipmentSerializer(shipment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_shipment(self):
        response = client.get(
            reverse('shipment details', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_shipment(self):
        response = client.post(
            reverse('shipments list'),
            data=json.dumps(self.VALID_SHIPMENT_DATA),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('shipments list'),
            data=json.dumps(self.INVALID_SHIPMENT_DATA),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_shipment(self):
        response = client.put(
            reverse('shipment details', kwargs={'id': self.first_shipment.pk}),
            data=json.dumps(self.VALID_SHIPMENT_DATA),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_shipment(self):
        response = client.put(
            reverse('shipment details', kwargs={'id': self.first_shipment.pk}),
            data=json.dumps(self.INVALID_SHIPMENT_DATA),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_shipment(self):
        response = client.delete(
            reverse('shipment details', kwargs={'id': self.first_shipment.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_shipment(self):
        response = client.delete(
            reverse('shipment details', kwargs={'id': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)