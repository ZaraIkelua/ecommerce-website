from uuid import uuid4
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from utils.auth import login_required
from utils.models import OrderMapper
from .models import Product, Cart, CartProduct, Order, OrderProduct


# Create your views here.
def homepage(request):
    return render(request, "general/homepage.html")


def shop(request):
    return render(request, "general/shop.html", {'search': True})


def products_list(request):
    products = Product.objects
    search = request.GET.get("search", '')
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1
    try:
        per_page = int(request.GET.get("per_page", 10))
    except ValueError:
        per_page = 10

    if search and search.strip() != '':
        products = products.filter(Q(name__icontains=search) | Q(category__name__icontains=search))

    product_data = products.all()[(page - 1) * per_page: ((page - 1)
                                                          * per_page) + per_page]
    data = [dict(
        id=product.id,
        name=product.name,
        category=product.category.name,
        price=product.price,
        discount=product.discount,
        description=product.description[:30] + '...',
        image=product.image
    ) for product in product_data.all()]

    return JsonResponse({"response": data})


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'general/product_details.html', context)


@login_required
def add_to_cart(request):
    product_id = request.GET.get("product_id")
    try:
        product = Product.objects.get(pk=product_id)

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)

        try:
            qty = int(request.GET.get('qty', 1))
        except (ValueError, TypeError):
            qty = 1

        try:
            CartProduct.objects.create(cart=cart, product=product, quantity=qty)
        except Exception:
            messages.error(request, "Product already in the cart.")
            return redirect(request, 'product_details', pk=product.pk)
        messages.success(request, "Added to cart.")
        return redirect('product_details', pk=product.pk)
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist.")
        return redirect("homepage")
    except Exception:
        messages.error(request, "Failed to add this product in cart")
        return redirect('product_details', pk=product_id)
    

@login_required
def cart(request):
    carts = CartProduct.objects.filter(cart__user=request.user)
    search = request.GET.get('search', '')
    if search and search.strip() != '':
        carts = carts.filter(product__name__icontains=search)
    context = {"cart": carts, 'search': True}
    return render(request, 'general/cart.html', context)


@login_required
def delete_from_cart(request):
    cart_id = request.GET.get("cart")
    try:
        cartporduct = CartProduct.objects.get(id=cart_id)
        cartporduct.delete()
        messages.success(request, "Product removed successfully.")
        return redirect('cart')
    except Exception as error:
        messages.error(request, "Failed to delete product from cart.")
        return redirect("cart")


@login_required
def checkout(request):
    cart_products = CartProduct.objects.filter(cart__user=request.user)
    total_price = sum([product.product.price * product.quantity for product in cart_products])
    total_discount = sum([(product.product.price * (product.product.discount / 100)) * product.quantity for product in cart_products])
    final = total_price - total_discount
    return render(request, 'general/checkout.html',
                  {"total_price": total_price, "total_discount": total_discount, 'final': final})


@login_required
def final_order(request):
    try:
        order = Order.objects.create(user=request.user, transaction_id=uuid4())
        carts = CartProduct.objects.filter(cart__user=request.user)
        for cartproduct in carts:
            OrderProduct.objects.create(
                order=order,
                product=cartproduct.product,
                quantity=cartproduct.quantity,
                price=cartproduct.product.price,
                discount=cartproduct.product.discount,
                final_price=cartproduct.product.price - ((cartproduct.product.price * cartproduct.product.discount) / 100)
            )
            cartproduct.delete()
        

        messages.success(request, "Order placed successfully!")
        return redirect('shop')
    except Exception as error:
        messages.error(request, str(error))
        return redirect('shop')

@login_required
def order(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders': [OrderMapper(order) for order in orders]}
    return render(request, "general/order.html", context)
