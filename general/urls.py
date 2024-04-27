from django.urls import path

from general import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("shop/", views.shop, name="shop"),
    path("products/", views.products_list, name="products"),
    path("product/<int:pk>", views.product_details, name="product_details"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
    path("delete_from_cart", views.delete_from_cart, name="delete_from_cart"),
    path("checkout", views.checkout, name="checkout"),
    path("final_order", views.final_order, name="final_order"),
    path("order", views.order, name='order'),
]