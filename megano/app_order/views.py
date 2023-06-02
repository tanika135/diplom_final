import json

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product
from app_catalog.views import get_product_data
from app_order.models import Order, OrderItems


def orders(request):
    if request.method == "POST":
        '''вызывается при нажатии оформить заказ в корзине'''
        new_order = Order.objects.create()
        items = json.loads(request.body)
        product_ids = [item["id"] for item in items]

        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            OrderItems.objects.create(order=new_order, product=product)

        data = {
          "orderId": new_order.pk
        }
        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        '''вызывается в профиле на странице списка заказов'''
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
        '''вызывается при переходе на страницу заполнения полей заказа'''
        order = Order.objects.get(pk=id)

        product_list = []
        for item in order.items.all():
            product = item.product
            product_data = get_product_data(product)
            product_data["reviews"] = product.reviews.count()
            product_list.append(
                product_data
            )

        #todo: вывести остальные поля из заказа - создать поля в модели


        data = {
            "id": order.pk,
            "createdAt": order.created,
            "fullName": "Annoying Orange",
            "email": "no-reply@mail.ru",
            "phone": "88002000600",
            "deliveryType": "free",
            "paymentType": "online",
            "totalCost": 567.8,
            "status": "accepted",
            "city": "Moscow",
            "address": "red square 1",
            "products": product_list
        }
        return JsonResponse(data)

    elif request.method == 'POST':

        ''' вызывается в самом конце оформления заказа, переде переходом к оплате'''
        order_fields = json.loads(request.body)
        order = Order.objects.get(pk=id)
        order.full_name = order_fields['fullName']
        #todo: заполнить остальные поля



        order.save()

        data = {"orderId": order.pk}
        return JsonResponse(data)

    return HttpResponse(status=500)


def payment(request, id):
    print('qweqwewqeqwe', id)
    return HttpResponse(status=200)
