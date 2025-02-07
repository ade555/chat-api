from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UsersList, RegisterUser

urlpatterns = [
    path('', UsersList.as_view(), name="all-users"),
    path('signup/', RegisterUser.as_view(), name="user-registration"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]