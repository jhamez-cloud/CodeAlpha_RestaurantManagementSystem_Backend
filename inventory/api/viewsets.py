from config.viewsets import StandardViewset
from inventory.serializers import InventorySerializer
from inventory.models import Inventory

class InventoryViewset(StandardViewset):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer