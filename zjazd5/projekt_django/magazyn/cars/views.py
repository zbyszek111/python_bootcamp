from django.shortcuts import render

# Create your views here.

from cars.models import Cars

def cars_list(request):
    cars = Cars.objects.all()
    return render(
        request=request,
        context={'cars': cars},
        template_name='cars_list.html'
    )

def car_details(request):
    car = Cars.objests.all()


def product_details(request, id):
    product = Product.objects.get(pk=id)
    output = f"Product: {product.id}<br><br>"
    output += f"Name: {product.name}<br>"
    output += f"Description: {product.description}<br>"
    output += f"Is available: {product.is_available}<br>"