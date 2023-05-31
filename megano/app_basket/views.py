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
        id = body['id']
        count = int(body['count'])

        product = Product.objects.get(pk=id)
        if not product:
            return HttpResponse(status=400)

        cart.add(product, count)
        cart.save()
        data = get_cart_data(cart)
        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        body = json.loads(request.body)
        id = body['id']
        print('[DELETE] /api/basket/')
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500.67,
                "count": 11,
                "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                "title": "video card",
                "description": "description of the product",
                "freeDelivery": True,
                "images": [
                    {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "hello alt",
                    }
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "Hello world"
                    }
                ],
                "reviews": 5,
                "rating": 4.6
            }
        ]
        return JsonResponse(data, safe=False)
