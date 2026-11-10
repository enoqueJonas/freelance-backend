from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UsernameOrEmailTokenSerializer


class UsernameOrEmailTokenView(TokenObtainPairView):
    serializer_class = UsernameOrEmailTokenSerializer
