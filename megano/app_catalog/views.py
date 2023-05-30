import json
from datetime import datetime
from math import ceil
from random import randrange

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product, Category, ProductReviews, Tag
from django.db.models import Count


def categories(request):
    if request.method == 'GET':
        categories = Category.objects.filter(parent=None)
        data = []
        for category in categories:
            subcategories = []
            for subcategory in category.children.all():
                subcategories.append({
                    "id": subcategory.id,
                    "title": subcategory.title,
                    "image": {
                        "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                        "alt": "Image alt string"
                    }
                })

            data.append({
                "id": category.id,
                "title": category.title,
                "subcategories": subcategories,
                "image": {
                    "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                    "alt": "Image alt string"
                }
            })

        return JsonResponse(data, safe=False)


def catalog(request):
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
        print(params.getlist('tags[]'))
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

    for product in products[start:end]:
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
    product = get_product(id)
    if request.method == 'GET':
        data = get_product_data(product)
        data["reviews"] = get_reviews(product)
        return JsonResponse(data)
    else:
        return HttpResponse(status=400)


def get_product(product_id):
    product = Product.objects.get(pk=product_id)
    if not product:
        return None
    else:
        return product


def get_product_images(product):
    product_images = []
    for image in product.images.all():
        product_images.append({
            "src": image.images.url,
            "alt": product.title,
        })
    if not product_images:
        product_images.append({
            "src": '/media/no_image.jpg',
            "alt": product.title,
        })
    return product_images


def get_product_tags(product):
    product_tags = []
    for tag in product.tags.all():
        product_tags.append({
            'id': tag.pk,
            'name': tag.name
        })
    return product_tags


def get_product_data(product):
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
    reviews = []
    for review in ProductReviews.objects.filter(product=product):
        reviews.append({
            "author": review.author,
            "email": review.email,
            "text": review.text,
            "rate": review.rate,
            "date": review.date,
        })
    return reviews


def product_reviews(request, id):
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
    data = []
    if request.method == 'GET':
        for tag in Tag.objects.filter(popular=True):
            data.append({
                "id": tag.id,
                "name": tag.name
            })
    return JsonResponse(data, safe=False)
