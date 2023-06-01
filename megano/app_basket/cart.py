from app_basket.models import CartItem


class Cart:
    def __init__(self, request):
        """ Инициализируем корзину """

        if not request.session.session_key:
            request.session.create()

        self.cart_user_id = request.session.session_key

    def __iter__(self):
        """ Перебор элементов в корзине и получение продуктов из базы данных. """
        items = CartItem.objects.filter(cart_id=self.cart_user_id)
        for item in items:
            item = {
                'product': item.product,
                'quantity': item.quantity,
            }
            yield item

    def add(self, product, quantity=1, update_quantity=False) -> int:
        """ Добавить продукт в корзину или обновить его количество. """
        try:
            product_in_cart = CartItem.objects.get(cart_id=self.cart_user_id, product=product)
            if update_quantity:
                product_in_cart.quantity = quantity
            else:
                product_in_cart.quantity += quantity
            product_in_cart.save()

        except CartItem.DoesNotExist:
            product_in_cart = CartItem.objects.create(cart_id=self.cart_user_id, product=product,
                                                      quantity=quantity, price=product.price)

        return product_in_cart.pk

    def remove(self, product) -> bool:
        """ Удаление товара из корзины. """
        try:
            product_in_cart = CartItem.objects.get(cart_id=self.cart_user_id, product=product)
            product_in_cart.delete()
            return True
        except CartItem.DoesNotExist:
            return False

    def clear(self) -> bool:
        """ удаление корзины """
        items = CartItem.objects.filter(cart_id=self.cart_user_id)
        for item in items:
            item.delete()
        return True

    def __len__(self):
        """ Подсчет всех товаров в корзине. """
        return CartItem.objects.filter(cart_id=self.cart_user_id).count()
