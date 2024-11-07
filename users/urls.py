from .views import StaffRegistrationView, ManagerRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
urlpatterns = [
    path('staff/', StaffRegistrationView.as_view(), name='staff_registration'),
    path('manager/', ManagerRegistrationView.as_view(), name='manager_registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]