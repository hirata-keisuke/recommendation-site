from django.urls import path

from recommendations import views

urlpatterns = [
    path("style/regist/", views.regist_style, name="regist_style"),
    path("style/<int:style_id>/", views.detail_style, name="detail_style"),
    path("style/<int:style_id>/edit/", views.edit_style, name="edit_style"),
    path("brand/regist/", views.regist_brand, name="regist_brand"),
    path("brand/<int:brand_id>/", views.detail_brand, name="detail_brand"),
]
