from rest_framework.routers import DefaultRouter
from .api.viewsets import RecipeViewset

router = DefaultRouter()
router.register(r'recipe',RecipeViewset,basename='recipes')

urlpatterns = router.urls