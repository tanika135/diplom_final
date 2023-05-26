from random import randrange

from django.http import JsonResponse
from django.shortcuts import render


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

