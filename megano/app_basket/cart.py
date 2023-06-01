from decimal import Decimal
from django.conf import settings
from app_catalog.models import Product


class Cart(object):

    def __init__(self, request):
        """ Инициализируем корзину """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """ Добавить продукт в корзину или обновить его количество. """
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = 0

        if update_quantity:
            self.cart[product_id] = quantity
        else:
            self.cart[product_id] += quantity
        self.save()

    def save(self):
        """ Обновление сессии cart """
        self.session[settings.CART_SESSION_ID] = self.cart
        """ Отметить сеанс как "измененный", чтобы убедиться, что он сохранен """
        self.session.modified = True

    def remove(self, product):
        """ Удаление товара из корзины. """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """ Перебор элементов в корзине и получение продуктов из базы данных. """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            item = {
                'product': product,
                'quantity': self.cart[str(product.id)],
            }
            yield item

    def __len__(self):
        """ Подсчет всех товаров в корзине. """
        return len(self.cart)

    # def get_total_price(self):
    #     """ Подсчет стоимости товаров в корзине. """
    #     return sum(Decimal(item['price']) * self.get_item_quantity(item) for item in
    #                self.cart.values())

    def clear(self):
        """ удаление корзины из сессии. """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

