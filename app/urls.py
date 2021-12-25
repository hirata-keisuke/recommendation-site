from django.urls import path, reverse

from . import views

app_name = "app"
urlpatterns = [
    path("top/", views.top, name="top"),
    path("login/", views.login, name="login"),
    path("logout/", views.login_check, name="login_check"),
    path("logout/", views.logout, name="logout"),
    path("search/", views.search, name="search"),
    path("search_result/", views.search_result, name="search_result"),
    path("overview/", views.overview, name="overview"),
]
