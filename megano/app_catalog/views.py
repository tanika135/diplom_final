import json
from datetime import datetime
from math import ceil
from random import randrange

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product, Category, ProductReviews, Tag, Specifications
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
        "specifications": get_specifications(product),
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


def get_specifications(product):
    """
    Формирование словаря с характеристиками к товару.
    """
    specifications = []
    for specification in product.specifications.all():
        specifications.append({
            "id": specification.id,
            'name': specification.name,
            'value': specification.value
        })
    return specifications


def product_specifications(request):
    """
    Добавление характеристик товара.
    """
    data = []
    if request.method == 'GET':
        for specification in Specifications.objects.all():
            data.append({
                "id": specification.id,
                "name": specification.name,
                "value": specification.value
            })
    return JsonResponse(data, safe=False)


def products_popular(request):
    if request.method == 'GET':
        popular_products = []
        for popular in Product.objects.all().order_by('sort')[:8]:
            popular_products.append({
                "id": popular.id,
                "category": popular.category.id,
                "price": popular.price,
                "count": popular.count,
                "date": popular.date,
                "title": popular.title,
                "description": popular.description,
                "freeDelivery": popular.freeDelivery,
                "images": get_product_images(popular),
                "tags": get_product_tags(popular),
                "rating": popular.rating
            })
        return JsonResponse(popular_products, safe=False)


def products_limited(request):
    if request.method == 'GET':
        limited_edition = []
        for limited in Product.objects.filter(products_limited=True)[:8]:
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
        return JsonResponse(limited_edition, safe=False)


def banners(request):
    if request.method == 'GET':
        data = []
        for banner in Product.objects.filter(banner=True):
            data.append({
                "id": banner.id,
                "category": banner.category.id,
                "price": banner.price,
                "count": banner.count,
                "date": banner.date,
                "title": banner.title,
                "description": banner.description,
                "freeDelivery": banner.freeDelivery,
                "images": get_product_images(banner),
                "tags": get_product_tags(banner),
                "rating": banner.rating,
            })
        return JsonResponse(data, safe=False)


def sales(request):
    if request.method == 'GET':

        params = request.GET

        page_size = 8

        filter_args = {
            'saleStart__lt':datetime.now(),
            'saleEnd__gt': datetime.now()
        }

        cur_page = 1
        if "currentPage" in params:
            cur_page = int(params['currentPage'])

        start = (cur_page - 1) * page_size
        end = cur_page * page_size

        products_sale = []
        format = '%d-%m'
        sale_products = Product.objects.filter(**filter_args)
        total = sale_products.count()
        for product in sale_products[start:end]:
            products_sale.append({
                "id": product.id,
                "price": product.price,
                "salePrice": product.salePrice,
                "dateFrom": product.saleStart.strftime(format),
                "dateTo": product.saleEnd.strftime(format),
                "title": product.title,
                "images": get_product_images(product),
            })

        data = {
            'items': products_sale,
            'currentPage': cur_page,
            'lastPage': ceil(total/page_size),
        }
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status=400)
