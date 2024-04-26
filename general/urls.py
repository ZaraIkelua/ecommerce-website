from django.urls import path

from general import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("shop/", views.shop, name="shop"),
    path("products/", views.products_list, name="products")
]