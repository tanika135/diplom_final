from random import randrange

from django.http import JsonResponse
from django.shortcuts import render

from app_catalog.models import Product


def categories(request):
    data = [
        {
            "id": 123,
            "title": "video card",
            "image": {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "Image alt string"
            },
            "subcategories": [
                {
                    "id": 123,
                    "title": "video card",
                    "image": {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "Image alt string"
                    }
                }
            ]
        }
    ]
    return JsonResponse(data, safe=False)


def catalog(request):
    data = {
        "items": [
             {
                 "id": 123,
                 "category": 123,
                 "price": 500.67,
                 "count": 12,
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
        ],
        "currentPage": randrange(1, 4),
        "lastPage": 3
    }
    return JsonResponse(data)


def product(request, id):

    # product = get_product(id)
    product = get_product(1)

    if request.method == 'GET':
        data = {
            "id": product.id,
            "category": 55,
            "price": product.price,
            "count": product.count,
            "date": product.date,
            "title": product.title,
            "description": product.description,
            "fullDescription": product.fullDescription,
            "freeDelivery": product.freeDelivery,
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
            "reviews": [
                {
                    "author": "Annoying Orange",
                    "email": "no-reply@mail.ru",
                    "text": "rewrewrwerewrwerwerewrwerwer",
                    "rate": 4,
                    "date": "2023-05-05 12:12"
                }
            ],
            "specifications": [
                {
                    "name": "Size",
                    "value": "XL"
                }
            ],
            "rating": 4.6
        }
        return JsonResponse(data)


def get_product(product_id):
    product = Product.objects.get(pk=product_id)
    if not product:
        return None

    return product
