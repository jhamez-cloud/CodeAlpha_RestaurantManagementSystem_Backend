from rest_framework import status
from rest_framework.response import Response

from config.viewsets import StandardViewset
from order.serializers import OrderSerializer, OrderItemReadSerializer,OrderItemWriteSerializer
from order.models import Order, OrderItem

from inventory.services import InventoryService


class OrderItemViewset(StandardViewset):
    queryset = OrderItem.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return OrderItemReadSerializer
        return OrderItemWriteSerializer


class OrderViewset(StandardViewset):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)

        instance = self.get_object()

        old_status = instance.order_status

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )

        serializer.is_valid(raise_exception=True)

        new_status = serializer.validated_data.get(
            "order_status",
            old_status
        )

        # Deduct inventory only once
        if (
            old_status != Order.OrderStatus.PREPARING
            and new_status == Order.OrderStatus.PREPARING
        ):

            result = InventoryService.process_order(instance)

            if not result["success"]:
                return Response(
                    result,
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_update(serializer)

        return Response(serializer.data)