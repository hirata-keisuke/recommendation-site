from django.urls import path, reverse

from . import views

app_name = "app"
urlpatterns = [
    path("brand_detail/<int:pk>/", views.BrandDetail.as_view(), name="brand_detail"),
    path("brand_delete/<int:pk>", views.BrandDelete.as_view(), name="brand_delete"),
    path("brand_update/<int:pk>", views.BrandUpdate.as_view(), name="brand_update"),
    path("review_create/", views.ReviewCreate.as_view(), name="search_result"),
    path("brand_list/", views.BrandList.as_view(), name="brand_list"),
]
