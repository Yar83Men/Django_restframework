from django.contrib import admin
from django.urls import path, include

##############################
# /rest-auth/login/ (POST)
# username
# email
# password
# Returns Token key
##############################
# /rest-auth/logout/ (POST)
##############################
# /rest-auth/password/reset/ (POST)
# email
##############################
# /rest-auth/password/reset/confirm/ (POST)
# uid and token are sent in email after calling /rest-auth/password/reset/
# uid
# token
# new_password1
# new_password2
##############################
# /rest-auth/password/change/ (POST)
# new_password1
# new_password2
# old_password
##############################
# /rest-auth/user/ (GET, PUT, PATCH)
# username
# first_name
# last_name
# Returns pk, username, email, first_name, last_name
##############################
# Registration
# /rest-auth/registration/ (POST)
# username
# password1
# password2
# email
# /rest-auth/registration/verify-email/ (POST)
# key

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('app/', include('app.urls')),
    path('car/', include('car.urls')),
    path('posts/', include('posts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('collage/', include('collage.urls')),
    path('racing/', include('racing.urls'))
]
