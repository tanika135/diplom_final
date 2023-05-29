import json
from datetime import datetime
from random import randrange

from django.http import JsonResponse, HttpResponse

from app_catalog.models import Product, Category, ProductReviews


def categories(request):
    categories = Category.objects.filter(parent=None)
    data = []
    for category in categories:
        subcategories = []
        for subcategory in category.children.all():
            subcategories.append({
                "id": subcategory.id,
                "title": subcategory.title,
                # "image": {
                #     "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                #     "alt": "Image alt string"
            })

        data.append({
            "id": category.id,
            "title": category.title,
            "subcategories": subcategories,
            # "image": {
            #     "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
            #     "alt": "Image alt string"
        })

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


def product(request, id):

    # product = get_product(id)
    product = get_product(1)

    if request.method == 'GET':
        product_images = []
        for image in product.images.all():
            product_images.append({
                "src": image.images.url,
                "alt": product.title,
            })

        reviews_on_product = get_reviews(product)


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
            "tags": [
                    {
                        "id": 0,
                        "name": "Hello world"
                    }
             ],
            "reviews": reviews_on_product,
            "specifications": [
                {
                    "name": "Size",
                    "value": "XL"
                }
            ],
            "rating": 4.6
        }
        return JsonResponse(data)


def get_product(product_id):
    product = Product.objects.get(pk=product_id)
    if not product:
        return None
    else:
        return product


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
            review = ProductReviews.objects.create(author=author, email=email, text=text, rate=rate, product=product)
            data = get_reviews(product)

        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(status=400)

