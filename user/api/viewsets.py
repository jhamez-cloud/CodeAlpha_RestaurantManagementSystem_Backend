from config.viewsets import StandardViewset
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers import UserSerializer

class UserViewset(StandardViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)