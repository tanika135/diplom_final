import json

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product
from app_catalog.views import get_product_data
from app_order.models import Order, OrderItems, OrderStatus


def orders(request):
    if request.method == "POST":
        '''вызывается при нажатии оформить заказ в корзине'''
        status = OrderStatus.objects.get(code='new')
        new_order = Order.objects.create(status=status, user=request.user)

        items = json.loads(request.body)
        for item in items:
            product_id = int(item["id"])
            product_count = int(item["count"])
            product = Product.objects.get(pk=product_id)
            OrderItems.objects.create(order=new_order, product=product, count=product_count, price=product.price)

        data = {
          "orderId": new_order.pk
        }
        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        '''вызывается в профиле на странице списка заказов'''
        orders = Order.objects.filter(user=request.user)
        data = [get_order_data(order) for order in orders]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = {
            "orderId": 123,
        }
        return JsonResponse(data)

    return HttpResponse(status=500)


def get_order_data(order):
    total_cost = 0
    product_list = []
    for item in order.items.all():
        product = item.product
        product_data = get_product_data(product)
        total_cost += item.price * item.count
        product_data["reviews"] = product.reviews.count()
        product_list.append(
            product_data
        )
    phone = ''
    if order.phone:
        phone = str(order.phone)
    data = {
        "id": order.pk,
        "createdAt": order.created,
        "fullName": order.full_name,
        "email": order.email,
        "phone": phone,
        "deliveryType": order.get_delivery_type_display(),
        "paymentType": order.get_payment_type_display(),
        "totalCost": total_cost,
        "status": order.status.title,
        "city": order.city,
        "address": order.address,
        "products": product_list
    }
    return data


def order(request, id):
    if request.method == 'GET':
        '''вызывается при переходе на страницу заполнения полей заказа'''
        order = Order.objects.get(pk=id)
        data = get_order_data(order)
        return JsonResponse(data)

    elif request.method == 'POST':

        ''' вызывается в самом конце оформления заказа, переде переходом к оплате'''
        order_fields = json.loads(request.body)
        order = Order.objects.get(pk=id)
        order.full_name = order_fields['fullName']
        order.email = order_fields['email']
        order.phone = order_fields['phone']
        order.delivery_type = order_fields['deliveryType']
        order.payment_type = order_fields['paymentType']
        order.city = order_fields['city']
        order.address = order_fields['address']
        order.save()

        data = {"orderId": order.pk}
        return JsonResponse(data)

    return HttpResponse(status=500)


def payment(request, id):
    payment_fields = json.loads(request.body)
    card_num = int(payment_fields["number"][-1:])
    if card_num % 2 == 0 and card_num != 0:
        order = Order.objects.get(pk=id)
        order.status = OrderStatus.objects.get(code='payed')
        order.save()
        print('qweqwewqeqwe', id)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

