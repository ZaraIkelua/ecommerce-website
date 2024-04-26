from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def homepage(request):
    return render(request, "general/homepage.html")


def shop(request):
    return render(request, "general/shop.html")


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
        name=product.name,
        category=product.category.name,
        price=product.price,
        discount=product.discount,
        description=product.description[:30] + '...',
        image=product.image.url
    ) for product in product_data.all()]

    return JsonResponse({"response": data})
