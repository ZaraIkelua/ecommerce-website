from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "general/homepage.html")


def shop(request):
    return render(request, "general/shop.html")


