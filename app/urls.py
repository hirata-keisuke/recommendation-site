from django.urls import path, reverse

from . import views

app_name = "app"
urlpatterns = [
    path("toplist/", views.TopList.as_view(), name="top_list"),
    path("style_list/", views.StyleList.as_view(), name="style_list"),
    path("style_detail/<int:pk>/", views.StyleDetail.as_view(), name="style_detail"),
    path("brand_search/", views.BrandSearch.as_view(), name="brand_search"),
    path("brand_detail/<int:pk>/", views.BrandDetail.as_view(), name="brand_detail"),
    path("review_create/", views.ReviewCreate.as_view(), name="review_create"),
    path("review_update/", views.ReviewUpdate.as_view(), name="review_update"),
    path("review_check/", views.ReviewCheck.as_view(), name="review_check"),
    path("review_complete/", views.ReviewComplete.as_view(), name="review_complete"),
    path("review_delete/", views.ReviewDelete.as_view(), name="review_delete"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("error/", views.Error.as_view(), name="error"),
]
