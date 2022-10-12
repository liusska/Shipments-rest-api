from django.db import models
from django.core.validators import MinLengthValidator


class Shipment(models.Model):
    SHIPMENT_REF_MAX_LENGTH = 50
    SHIPMENT_REF_MIN_LENGTH = 1
    DELIVERY_TOWN_MAX_LENGTH = 50
    DELIVERY_TOWN_MIN_LENGTH = 1
    DELIVERY_DATE_MAX_LENGTH = 20
    DELIVERY_DATE_MIN_LENGTH = 1
    BAYER_MAX_LENGTH = 50
    BAYER_MIN_LENGTH = 1
    SELLER_MAX_LENGTH = 50
    SELLER_MIN_LENGTH = 1
    DESCRIPTION_MAX_LENGTH = 300

    STATUS_CHOICE_IN_PROGRESS = 'In progress'
    STATUS_CHOICE_OUT_FOR_DELIVERY = 'Out for delivery'
    STATUS_CHOICE_DELIVERED = "Delivered"

    STATUS_LIST = [(x, x) for x in
             (
                 STATUS_CHOICE_IN_PROGRESS,
                 STATUS_CHOICE_OUT_FOR_DELIVERY,
                 STATUS_CHOICE_DELIVERED
             )]

    shipment_ref = models.CharField(
        max_length=SHIPMENT_REF_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(SHIPMENT_REF_MIN_LENGTH),
        )
    )

    delivery_date = models.CharField(
        max_length=DELIVERY_DATE_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(DELIVERY_DATE_MIN_LENGTH),
        )
    )
    delivery_town = models.CharField(
        max_length=DELIVERY_TOWN_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(DELIVERY_TOWN_MIN_LENGTH),
        )
    )
    bayer = models.CharField(
        max_length=BAYER_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(BAYER_MIN_LENGTH),
        )
    )
    seller = models.CharField(
        max_length=SELLER_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(SELLER_MIN_LENGTH),
        )
    )

    status = models.CharField(
        max_length=max(len(x) for (x, _) in STATUS_LIST),
        default=STATUS_CHOICE_IN_PROGRESS,
        choices=STATUS_LIST,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        default=""
    )

    def deliver_information(self):
        return f"Deliver information: From: {self.seller}, to {self.bayer} is in status: {self.status}"

    def __str__(self):
        return f"Ref.{self.shipment_ref} | status: {self.status}"
