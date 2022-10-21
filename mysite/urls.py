from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   path('admin/', admin.site.urls),
   path("accounts/", include("allauth.urls")), #most important
   path('', include("louslist.urls")), #my app urls
   #path('classes/',include("louslist.urls"))
]
