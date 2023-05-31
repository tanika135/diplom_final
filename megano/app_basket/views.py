from django.http import JsonResponse


def basket(request):
    if request.method == "GET":
        print('[GET] /api/basket/')
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
            },
            {
                "id": 124,
                "category": 55,
                "price": 201.675,
                "count": 5,
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

    elif request.method == "POST":
        body = json.loads(request.body)
        id = body['id']
        count = body['count']
        print('[POST] /api/basket/   |   id: {id}, count: {count}'.format(id=id, count=count))
        data = [
            {
                "id": id,
                "category": 55,
                "price": 500.67,
                "count": 13,
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
