from django.urls import path, include

from shipments_app.views import ShipmentsListView, DetailShipmentView

urlpatterns = (
    path('shipments/', ShipmentsListView.as_view(), name='shipments list'),
    path('shipments/<int:id>', DetailShipmentView.as_view(), name='shipment details'),
)