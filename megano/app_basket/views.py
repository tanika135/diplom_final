from django.http import JsonResponse, HttpResponse
import json
from app_basket.cart import Cart
from app_catalog.models import Product
from app_catalog.views import get_product_data


def get_cart_data(cart):
    data = []
    for item in cart:
        product_data = get_product_data(item['product'])
        product_data["count"] = item["quantity"]
        data.append(product_data)
    return data


def basket(request):
    cart = Cart(request)
    if request.method == "GET":
        data = get_cart_data(cart)
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        product_id = body['id']
        count = int(body['count'])

        product = Product.objects.get(pk=product_id)
        if not product:
            return HttpResponse(status=400)

        cart.add(product, count)
        data = get_cart_data(cart)
        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        body = json.loads(request.body)
        product_id = body['id']

        product = Product.objects.get(pk=product_id)
        if not product:
            return HttpResponse(status=400)

        cart.remove(product)
        data = get_cart_data(cart)
        return JsonResponse(data, safe=False)
