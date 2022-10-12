from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentsListView(APIView):
    def get(self, request):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ShipmentSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailShipmentView(APIView):
    def get(self, request, id):
        try:
            shipment = Shipment.objects.get(pk=id)
            serializer = ShipmentSerializer(shipment)
            return Response(serializer.data)
        except Shipment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        shipment = Shipment.objects.get(pk=id)
        serializer = ShipmentSerializer(shipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            shipment = Shipment.objects.get(pk=id)
            shipment.delete()
            return Response(status=status.HTTP_200_OK)
        except Shipment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
