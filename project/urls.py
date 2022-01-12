from django.contrib import admin
from django.urls import path, include

from recommendations import views

urlpatterns = [
    path("", views.top, name="top"),
    path('admin/', admin.site.urls),
    path("recommendations/", include("recommendations.urls")),
]
