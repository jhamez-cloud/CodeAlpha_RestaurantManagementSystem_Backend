from config.viewsets import StandardViewset
from menu.serializers import MenuCategorySerializer,MenuItemSerializer
from menu.models import MenuItem,MenuCategory

class MenuCategoryViewset(StandardViewset):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemViewset(StandardViewset):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer