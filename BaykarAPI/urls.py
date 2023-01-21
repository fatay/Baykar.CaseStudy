from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView

# Define url regex patterns for handling requests.
# Also, include urls that defined by applications (appname.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('BaykarApp.urls')),
    re_path(r'^register/', include('rest_auth.registration.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]

