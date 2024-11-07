from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import StaffRegistrationSerializer, ManagerRegistrationSerializer

class StaffRegistrationView(generics.CreateAPIView):
    serializer_class = StaffRegistrationSerializer
    permission_classes = [AllowAny]

class ManagerRegistrationView(generics.CreateAPIView):
    serializer_class = ManagerRegistrationSerializer
    permission_classes = [AllowAny]
