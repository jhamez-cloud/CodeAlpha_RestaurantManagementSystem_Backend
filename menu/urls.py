from rest_framework.routers import DefaultRouter
from .api.viewsets import MenuCategoryViewset,MenuItemViewset

router = DefaultRouter()
router.register(r'menu-category',MenuCategoryViewset,basename='menucategory')
router.register(r'menu-item',MenuItemViewset,basename='menuitem')

urlpatterns = router.urls