from config.viewsets import StandardViewset
from user.models import User
from user.serializers import UserSerializer

class UserViewset(StandardViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer