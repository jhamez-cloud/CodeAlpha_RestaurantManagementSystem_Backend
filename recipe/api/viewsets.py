from config.viewsets import StandardViewset
from recipe.serializers import RecipeSerializer
from recipe.models import Recipe


class RecipeViewset(StandardViewset):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer