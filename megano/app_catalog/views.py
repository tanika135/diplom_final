import json
from datetime import datetime
from math import ceil
from random import randrange

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product, Category, ProductReviews, Tag
from django.db.models import Count


def get_category_data(category):
    """
    Формирование словаря с вложенностью категорий.
    :param category:
    :return:
    """
    data = {}
    subcats = []
    for subcategory in category.children.all():
        subcats.append(get_category_data(subcategory))

    if category.image:
        image = category.image.url
    else:
        image = '/media/no_image.svg'

    cat_data = {
        "id": category.id,
        "title": category.title,
        "subcategories": subcats,
        "image": {
            "src": image,
            "alt": category.title
        }
    }

    return cat_data


def categories(request):
    """
    Функция представления категорий.
    :param request:
    :return:
    """
    if request.method == 'GET':
        categories = Category.objects.filter(parent=None)
        data = []
        for category in categories:
            data.append(get_category_data(category))
        return JsonResponse(data, safe=False)


def catalog(request):
    """
    Фильтрация и сортировка товаров в каталоге.
    :param request:
    :return:
    """
    params = request.GET

    page_size = 20
    if "limit" in params:
        page_size = int(params['limit'])

    filter_args = {}

    cur_page = 1
    if "currentPage" in params:
        cur_page = int(params['currentPage'])
    start = (cur_page - 1) * page_size
    end = cur_page * page_size

    if "filter[name]" in params:
        filter_args['title__icontains'] = params.get('filter[name]')

    if "filter[minPrice]" in params:
        filter_args['price__gte'] = params.get('filter[minPrice]')

    if "filter[maxPrice]" in params:
        filter_args['price__lte'] = params.get('filter[maxPrice]')

    if "filter[freeDelivery]" in params and params.get('filter[freeDelivery]') == 'true':
        filter_args['freeDelivery'] = True

    if "filter[available]" in params and params.get('filter[available]') == 'true':
        filter_args['count__gt'] = 0

    if 'tags[]' in params:
         filter_args['tags__id__in'] = params.getlist('tags[]')

    sorting = 'price'
    if 'sort' in params:
        if params.get('sortType') == 'inc':
            order = ''
        else:
            order = '-'
        sort = params.get('sort')
        if sort == 'reviews':
            sort = 'num_reviews'
        sorting = order + sort

    products = Product.objects.filter(**filter_args).annotate(num_reviews=Count('reviews')).order_by(sorting)
    total = products.count()
    product_list = []

    page_products = products[start:end]
    for product in page_products:
        product_data = get_product_data(product)
        product_data["reviews"] = product.reviews.count()
        product_list.append(
            product_data
        )

    data = {
        "items": product_list,
        "currentPage": cur_page,
        "lastPage": ceil(total/page_size)
    }
    return JsonResponse(data)


def product(request, id):
    """
    Представление карточки товара.
    :param request:
    :param id:
    :return:
    """
    product = get_product(id)
    if request.method == 'GET':
        data = get_product_data(product)
        data["reviews"] = get_reviews(product)
        return JsonResponse(data)
    else:
        return HttpResponse(status=400)


def get_product(product_id):
    """
    Загрузка товара из базы по id.

    """
    product = Product.objects.get(pk=product_id)
    if not product:
        return None
    else:
        return product


def get_product_images(product):
    """
    Загрузка изображений.
    :param product:
    :return:
    """
    product_images = []
    for image in product.images.all():
        product_images.append({
            "src": image.images.url,
            "alt": product.title,
        })
    if not product_images:
        product_images.append({
            "src": '/media/no_image.svg',
            "alt": product.title,
        })
    return product_images


def get_product_tags(product):
    """
    Загрузка тегов.
    :param product:
    :return:
    """
    product_tags = []
    for tag in product.tags.all():
        product_tags.append({
            'id': tag.pk,
            'name': tag.name
        })
    return product_tags


def get_product_data(product):
    """
    Формирование словаря с товаром.
    :param product:
    :return:
    """
    product_images = get_product_images(product)
    data = {
        "id": product.id,
        "category": product.category.id,
        "price": product.price,
        "count": product.count,
        "date": product.date,
        "title": product.title,
        "description": product.description,
        "fullDescription": product.fullDescription,
        "freeDelivery": product.freeDelivery,
        "images": product_images,
        "tags": get_product_tags(product),
        "specifications": [
            {
                "name": "Size",
                "value": "XL"
            }
        ],
        "rating": product.rating
    }
    return data


def get_reviews(product:Product) -> list:
    """
    Формирование словаря с отзывом к товару.
    """
    reviews = []
    for review in product.reviews.all():
        reviews.append({
            "author": review.author,
            "email": review.email,
            "text": review.text,
            "rate": review.rate,
            "date": review.date,
        })
    return reviews


def product_reviews(request, id):
    """
    Добавление отзывов.
    """
    if request.method == 'POST':
        data = []
        body = json.loads(request.body)
        author = body['author']
        email = body['email']
        text = body['text']
        rate = body['rate']

        product = Product.objects.get(pk=id)
        if product:
            ProductReviews.objects.create(author=author, email=email, text=text, rate=rate, product=product)
            data = get_reviews(product)

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status=400)


def tags(request):
    """
    Функция для получения популярных тегов.
    """
    data = []
    if request.method == 'GET':
        for tag in Tag.objects.filter(popular=True):
            data.append({
                "id": tag.id,
                "name": tag.name
            })
    return JsonResponse(data, safe=False)


def products_popular(request):

    data = [
        {
            "id": "123",
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


def products_limited(request):
    if request.method == 'GET':
        limited_edition = []
        for limited in Product.objects.filter(products_limited=True):
            limited_edition.append({
                "id": limited.id,
                "category": limited.category.id,
                "price": limited.price,
                "count": limited.count,
                "date": limited.date,
                "title": limited.title,
                "description": limited.description,
                "freeDelivery": limited.freeDelivery,
                "images": get_product_images(limited),
                "tags": get_product_tags(limited),
                "rating": limited.rating
            })
        # limited_edition = [
        #     {
        #         "id": "123",
        #         "category": 55,
        #         "price": 500.67,
        #         "count": 12,
        #         "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        #         "title": "video card",
        #         "description": "description of the product",
        #         "freeDelivery": True,
        #         "images": [
        #                 {
        #                     "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
        #                     "alt": "hello alt",
        #                 }
        #          ],
        #         "tags": [
        #                 {
        #                     "id": 0,
        #                     "name": "Hello world"
        #                 }
        #         ],
        #         "reviews": 5,
        #         "rating": 4.6
        #     }
        # ]
        return JsonResponse(limited_edition, safe=False)
