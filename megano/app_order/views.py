from django.http import JsonResponse, HttpResponse


def orders(request):
    if request.method == "POST":
        data = [
            {
                "id": 123,
                "category": 55,
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
        ]
        return JsonResponse(data, safe=False)


def orders(request):
    if request.method == 'GET':
        data = [
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string"
                            }
                        ],
                        "tags": [
                            {
                                "id": 12,
                                "name": "Gaming"
                            }
                        ],
                        "reviews": 5,
                        "rating": 4.6
                    }
                ]
            },
            {
                "id": 123,
                "createdAt": "2023-05-05 12:12",
                "fullName": "Annoying Orange",
                "email": "no-reply@mail.ru",
                "phone": "88002000600",
                "deliveryType": "free",
                "paymentType": "online",
                "totalCost": 567.8,
                "status": "accepted",
                "city": "Moscow",
                "address": "red square 1",
                "products": [
                    {
                        "id": 123,
                        "category": 55,
                        "price": 500.67,
                        "count": 12,
                        "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                        "title": "video card",
                        "description": "description of the product",
                        "freeDelivery": True,
                        "images": [
                            {
                                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                                "alt": "Image alt string"
                            }
                        ],
                        "tags": [
                            {
                                "id": 12,
                                "name": "Gaming"
                            }
                        ],
                        "reviews": 5,
                        "rating": 4.6
                    }
                ]
            }
        ]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = {
            "orderId": 123,
        }
        return JsonResponse(data)

    return HttpResponse(status=500)


def order(request, id):
    if request.method == 'GET':
        data = {
            "id": 123,
            "createdAt": "2023-05-05 12:12",
            "fullName": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "phone": "88002000600",
            "deliveryType": "free",
            "paymentType": "online",
            "totalCost": 567.8,
            "status": "accepted",
            "city": "Moscow",
            "address": "red square 1",
            "products": [
                {
                    "id": 123,
                    "category": 55,
                    "price": 500.67,
                    "count": 12,
                    "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
                    "title": "video card",
                    "description": "description of the product",
                    "freeDelivery": True,
                    "images": [
                        {
                            "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                            "alt": "Image alt string"
                        }
                    ],
                    "tags": [
                        {
                            "id": 12,
                            "name": "Gaming"
                        }
                    ],
                    "reviews": 5,
                    "rating": 4.6
                },
            ]
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        data = {"orderId": 123}
        return JsonResponse(data)

    return HttpResponse(status=500)


def payment(request, id):
    print('qweqwewqeqwe', id)
    return HttpResponse(status=200)
