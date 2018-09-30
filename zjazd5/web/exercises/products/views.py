from django.shortcuts import render, HttpResponse

# Create your views here.
from products.models import Product


def hello_world(request):
    return HttpResponse("Hello world")

def hello_world_name(request,name):
    return HttpResponse("Hello"+ name)

# def product_list(request):
#     products = Product.objects.all()
#     output =""
#
#     for prod in products:
#         output += f'{prod.id} | <a href="/products/{prod.id}">{prod.name}</a><br>'
#
#     return HttpResponse(output)

def products_list(request):
    products = Product.objects.all()
    return render(
        request,
        context={'products': products},
        template_name='products_list.html'
    )


def product_details(request, id):
    product = Product.objects.get(pk=id)
    output =  f"Product: {product.id}<br><br>"
    output += f"Name : {product.name}"
    output += f"Description : {product.description}"
    output += f"Is available : {product.is_available}"

    return HttpResponse(output)



